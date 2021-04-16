from src.core.types.info import Info


class ListViewModel:
    """View model for core type List."""

    def __init__(self, interpretation):
        """Create with value empty list.

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._interpretation = interpretation
        self._list = self._interpretation.info

    @property
    def value(self):
        """Readonly property for value."""
        return self._list

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

    def navigate_to(self, info: Info):
        self._interpretation.navigate(info)
