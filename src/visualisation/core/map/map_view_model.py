import logging

from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import \
    InterpretationService
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.navigation.navigation_proxy import NavigationProxy
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor
from src.black_fennec.structure.root_factory import RootFactory
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.type.type import Type
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.util.observable import Observable

logger = logging.getLogger(__name__)


class MapViewModel(Observable):
    """View model for core type Map."""

    def __init__(
            self,
            interpretation: Interpretation,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry
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
        self._map: Map = self._interpretation.structure
        logger.debug('Showing view for %s', str(self._map))

    @property
    def value(self):
        """Readonly property for value."""
        return self._map

    @value.setter
    def value(self, value: Map):
        self._map = value
        self._notify(self.value, 'value')

    @property
    def decapsulated_value(self):
        decapsulated_map = self.value
        while hasattr(decapsulated_map, 'subject'):
            decapsulated_map = decapsulated_map.subject
        return decapsulated_map

    @property
    def selected(self) -> Interpretation:
        return self._selected

    @selected.setter
    def selected(self, new_selected):
        self._notify(new_selected, 'selected')
        self._selected = new_selected

    def create_preview(self, substructure: Structure) -> Interpretation:
        """create preview for substructure

        Args:
            substructure (Structure): will be interpreted as a preview

        Returns:
            Interpretation: represents the substructure as preview
        """
        preview = self._interpretation_service.interpret(
            substructure, Specification(request_preview=True))
        navigation_proxy = NavigationProxy()
        navigation_proxy.bind(navigation_request=self.navigate)
        preview.set_navigation_service(navigation_proxy)
        return preview

    def add_item(self, key, value: Structure):
        """Add item (key, value) to the map.

        Args:
            key: The key under which to store the value.
            value (Structure): The `Structure` behind the key.
        """
        self.value.add_item(key, value)
        self._notify(self.value, 'value')

    def delete_item(self, key):
        """Delete an item from the map.

        Args:
            key: The key of the key value pair which should be deleted
        """
        self.value.remove_item(key)
        self._notify(self.value, 'value')

    def rename_key(self, old_key: str, new_key: str):
        """Rename the key of an item.

        Args:
            old_key (str): The key of the key value pair
                which should be renamed
            new_key (str): The new key name of the key value pair
        """
        map_with_retained_order = Map({})
        decapsulated_map = self.decapsulated_value

        if decapsulated_map.get_root() == decapsulated_map:
            RootFactory.make_root(map_with_retained_order, decapsulated_map.get_document())
        else:
            map_with_retained_order.parent = decapsulated_map.parent

        for key, value in decapsulated_map.value.items():
            if key == old_key:
                decapsulated_map.remove_item(key)
                map_with_retained_order.add_item(new_key, value)
            else:
                decapsulated_map.remove_item(key)
                map_with_retained_order.add_item(key, value)
        overlay = map_with_retained_order.accept(OverlayFactoryVisitor())
        self.value = overlay

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
