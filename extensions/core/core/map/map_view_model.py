import logging

from blackfennec.actions import ActionRegistry
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.interpretation_service import \
    InterpretationService
from blackfennec.interpretation.specification import Specification
from blackfennec.navigation.navigation_proxy import NavigationProxy
from blackfennec.structure.map import Map
from blackfennec.structure.structure import Structure
from blackfennec.type_system.type import Type
from blackfennec.type_system.type_registry import TypeRegistry
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class MapViewModel(Observable):
    """View model for core type Map."""

    def __init__(
            self,
            interpretation: Interpretation,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry,
            action_registry: ActionRegistry,
    ):
        """Create with value empty map.

        Args:
            interpretation (Interpretation): The overarching interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
            type_registry (TypeRegistry): registry used to
                add children to List from type.

        """
        Observable.__init__(self)
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        self._type_registry = type_registry
        self._action_registry = action_registry
        self._map: Map = self._interpretation.structure
        logger.debug('Showing view for %s', str(self._map))

    @property
    def value(self):
        """Readonly property for value."""
        return self._map

    @value.setter
    def value(self, value: Map):
        self._map = value
        self._notify('value', self.value)

    @property
    def selected(self) -> Interpretation:
        return self._selected

    @selected.setter
    def selected(self, new_selected):
        self._notify('selected', new_selected)
        self._selected = new_selected

    def create_interpretation(self, substructure: Structure) -> Interpretation:
        """create preview for substructure

        Args:
            substructure (Structure): will be interpreted as a preview

        Returns:
            Interpretation: represents the substructure as preview
        """
        interpretation = self._interpretation_service.interpret(
            substructure, Specification(request_preview=True))
        navigation_proxy = NavigationProxy()
        navigation_proxy.bind(navigation_request=self.navigate)
        interpretation.set_navigation_service(navigation_proxy)
        return interpretation

    def get_actions(self, substructure: Structure):
        types = self._interpretation_service.interpret(
            substructure,
            Specification(request_preview=True)
        ).types
        actions = set(
            action
            for type in types
            for action in self._action_registry.get_actions(type)
        )
        return actions

    def add_item(self, key, value: Structure):
        """Add item (key, value) to the map.

        Args:
            key: The key under which to store the value.
            value (Structure): The `Structure` behind the key.
        """
        self.value.add_item(key, value)
        self._notify('value', self.value)

    def delete_item(self, key):
        """Delete an item from the map.

        Args:
            key: The key of the key value pair which should be deleted
        """
        self.value.remove_item(key)
        self._notify('value', self.value)

    def rename_key(self, old_key: str, new_key: str):
        """Rename the key of an item.

        Args:
            old_key (str): The key of the key value pair
                which should be renamed
            new_key (str): The new key name of the key value pair
        """
        decapsulated_map = self.value.structure

        for key, value in decapsulated_map.value.items():
            decapsulated_map.remove_item(key)
            decapsulated_map.add_item(new_key if key == old_key else key, value)

    def _is_resolved_reference(self, key: str):
        return self.value.value[key].parent != self.value

    def add_by_template(self, key, template: Type):
        self.add_item(key, template.create_instance())

    def get_templates(self):
        return self._type_registry.types

    def navigate(self, sender, target: Structure):
        self.selected = sender
        self.navigate_to(target)

    def navigate_to(self, route_target: Structure):
        self._interpretation.navigate(route_target)
