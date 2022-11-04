# -*- coding: utf-8 -*-

from base.date_time.date_time_view import DateTimeView
from base.date_time.date_time_view_model import DateTimeViewModel
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.specification import Specification
from base.date_time.date_time_preview import DateTimePreview


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

    def create(self, interpretation: Interpretation) -> DateTimeView:
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

        if interpretation.specification.is_request_for_preview:
            return DateTimePreview(view_model)

        return DateTimeView(view_model)