from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification
from src.navigation.navigation_proxy import NavigationProxy
from src.structure.info import Info


class ListViewModel:
    """View model for core type List."""

    def __init__(self, interpretation, interpretation_service):
        """Create with value empty list.

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
        """
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        self._list = self._interpretation.info

    @property
    def value(self):
        """Readonly property for value."""
        return self._list

    def create_preview(self, substructure: Info) -> Interpretation:
        """create preview for substructure

        Args:
            substructure (Info): will be interpreted as a preview

        Returns:
            Interpretation: represents the substructure as preview
        """
        preview = self._interpretation_service.interpret(
            substructure, Specification(request_preview=True))
        navigation_proxy = NavigationProxy(self._interpretation)
        preview.set_navigation_service(navigation_proxy)
        return preview

    def add_item(self, value: Info):
        """Add item to the list.

        Args:
            value (:obj:`Info`): The `Info` representing the item.
        """
        self._list.append(value)

    def delete_item(self, item: Info):
        """Delete an item from the list.

        Args:
            item: The item which should be deleted
        """
        self._list.remove(item)

    def navigate_to(self, route_target: Info):
        self._interpretation.navigate(route_target)
