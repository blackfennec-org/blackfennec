# -*- coding: utf-8 -*-
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification
from src.type_system.base.date_time_range.date_time_range_view import DateTimeRangeView
from src.type_system.base.date_time_range.date_time_range_view_model import DateTimeRangeViewModel


class DateTimeRangeViewFactory:
    """Creator of the DateTimeRangeView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
               _: Specification) -> DateTimeRangeView:
        """creates a DateTimeRangeView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            DateTimeRangeView
        """
        view_model = DateTimeRangeViewModel(interpretation)
        return DateTimeRangeView(view_model)
