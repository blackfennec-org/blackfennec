# -*- coding: utf-8 -*-

from src.visualisation.base.date_time.date_time_view import DateTimeView
from src.visualisation.base.date_time.date_time_view_model import DateTimeViewModel
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class DateTimeViewFactory:
    """Creator of the DateTimeView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
            _: Specification) -> DateTimeView:
        """creates a DateTimeView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            DateTimeView
        """
        view_model = DateTimeViewModel(interpretation)
        return DateTimeView(view_model)
