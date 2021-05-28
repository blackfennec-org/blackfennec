# -*- coding: utf-8 -*-

from src.visualisation.base.date_time.date_time_view import DateTimeView
from src.visualisation.base.date_time.date_time_view_model import DateTimeViewModel
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.base.date_time.date_time_preview import DateTimePreview


class DateTimeViewFactory:
    """Creator of the DateTimeView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> DateTimeView:
        """creates a DateTimeView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            DateTimeView
        """
        view_model = DateTimeViewModel(interpretation)

        if specification.is_request_for_preview:
            return DateTimePreview(view_model)

        return DateTimeView(view_model)
