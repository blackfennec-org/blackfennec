from src.type_system.core.list.list_view_model import ListViewModel
from src.type_system.core.list.list_view import ListView

class ListViewFactory:
    """Creator of the ListView"""

    def create(self, interpretation) -> ListView:
        """creates a ListView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.

        Returns:
            :obj:`ListView`
        """
        view_model = ListViewModel(interpretation)
        return ListView(view_model)
