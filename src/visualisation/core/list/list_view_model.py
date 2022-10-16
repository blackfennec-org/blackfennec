from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import \
    InterpretationService
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.navigation.navigation_proxy import NavigationProxy
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.type.type import Type
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.util.observable import Observable


class ListViewModel(Observable):
    """View model for core type List."""

    def __init__(
            self,
            interpretation: Interpretation,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry
    ):
        """Create with value empty list.

        Args:
            interpretation (Interpretation): The overarching
                interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
            type_registry (TypeRegistry): registry used to
                add children to List from template.
        """
        Observable.__init__(self)
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        self._type_registry = type_registry
        self._list = self._interpretation.structure

    @property
    def value(self):
        """Readonly property for value."""
        return self._list

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

    def add_item(self, value: Structure):
        """Add item to the list.

        Args:
            value (Structure): The `Structure` representing the item.
        """
        self._list.add_item(value)
        self._notify(self.value, 'value')

    def delete_item(self, item: Structure):
        """Delete an item from the list.

        Args:
            item: The item which should be deleted
        """
        self._list.remove_item(item)
        self._notify(self.value, 'value')

    def add_by_template(self, template: Type):
        self.add_item(template.create_instance())

    def get_templates(self):
        return self._type_registry.types

    def navigate(self, sender, destination: Structure):
        self.selected = sender
        self.navigate_to(destination)

    def navigate_to(self, route_target: Structure):
        self._interpretation.navigate(route_target)

    def delete(self):
        raise NotImplementedError()
