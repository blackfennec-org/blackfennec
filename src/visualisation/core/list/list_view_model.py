from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import \
    InterpretationService
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.navigation.navigation_proxy import NavigationProxy
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.type_system.template_registry import TemplateRegistry
from src.black_fennec.util.observable import Observable


class ListViewModel(Observable):
    """View model for core type List."""

    def __init__(
            self,
            interpretation: Interpretation,
            interpretation_service: InterpretationService,
            template_registry: TemplateRegistry
    ):
        """Create with value empty list.

        Args:
            interpretation (Interpretation): The overarching
                interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
            template_registry (TemplateRegistry): registry used to
                add children to List from template.
        """
        Observable.__init__(self)
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        self._template_registry = template_registry
        self._list = self._interpretation.structure

    @property
    def value(self):
        """Readonly property for value."""
        return self._list

    def create_preview(self, substructure: Structure) -> Interpretation:
        """create preview for substructure

        Args:
            substructure (Structure): will be interpreted as a preview

        Returns:
            Interpretation: represents the substructure as preview
        """
        preview = self._interpretation_service.interpret(
            substructure, Specification(request_preview=True))
        navigation_proxy = NavigationProxy(self._interpretation)
        preview.set_navigation_service(navigation_proxy)
        return preview

    def add_item(self, value: Structure):
        """Add item to the list.

        Args:
            value (:obj:`Structure`): The `Structure` representing the item.
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

    def add_by_template(self, template: TemplateBase):
        self.add_item(template.create_structure())

    def get_templates(self):
        return self._template_registry.templates

    def navigate_to(self, route_target: Structure):
        self._interpretation.navigate(route_target)
