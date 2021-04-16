# -*- coding: utf-8 -*-

from src.type_system.base.date_time.date_time_view import DateTimeView
from src.type_system.base.date_time.date_time_view_model import DateTimeViewModel


class DateTimeViewFactory:
    """Creator of the DateTimeView"""

    def create(self, interpretation) -> DateTimeView:
        """creates a DateTimeView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            DateTimeView
        """
        view_model = DateTimeViewModel(interpretation)
        return DateTimeView(view_model)
