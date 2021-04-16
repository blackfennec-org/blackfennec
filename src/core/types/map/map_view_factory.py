from src.core.types.map import MapViewModel, MapView

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
