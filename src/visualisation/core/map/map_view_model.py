from src.black_fennec.structure.structure import Structure
from src.black_fennec.navigation.navigation_proxy import NavigationProxy
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.interpretation.interpretation import Interpretation


class MapViewModel:
    """View model for core type Map."""

    def __init__(self, interpretation, interpretation_service):
        """Create with value empty map.

        Args:
            interpretation (Interpretation): The overarching interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
        """
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        self._map = self._interpretation.structure

    @property
    def value(self):
        """Readonly property for value."""
        return self._map

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

    def add_item(self, key, value: Structure):
        """Add item (key, value) to the map.

        Args:
            key: The key under which to store the value.
            value (:obj:`Structure`): The `Structure` behind the key.
        """
        self._map[key] = value

    def delete_item(self, key):
        """Delete an item from the map.

        Args:
            key: The key of the key value pair which should be deleted
        """
        self._map.pop(key)

    def rename_key(self, old_key, new_key):
        """Rename the key of an item.

                Args:
                    old_key: The key of the key value pair which should be renamed
                    new_key: The new key name of the key value pair
                """
        self._map[new_key] = self._map.pop(old_key)

    def navigate_to(self, route_target: Structure):
        self._interpretation.navigate(route_target)
