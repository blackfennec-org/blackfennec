from src.core.map import MapViewModel, MapView

class MapViewFactory:
    """Creator or the MapView"""

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
