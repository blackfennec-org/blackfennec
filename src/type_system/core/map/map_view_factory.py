from src.type_system.core.map.map_view_model import MapViewModel
from src.type_system.core.map.map_view import MapView

class MapViewFactory:
    """Creator of the MapView"""

    def create(self, interpretation) -> MapView:
        """creates a MapView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.

        Returns:
            :obj:`MapView`
        """
        view_model = MapViewModel(interpretation)
        return MapView(view_model)
