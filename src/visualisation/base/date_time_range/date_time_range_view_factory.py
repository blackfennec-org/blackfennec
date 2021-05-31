# -*- coding: utf-8 -*-
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.base.date_time_range.date_time_range_preview import DateTimeRangePreview
from src.visualisation.base.date_time_range.date_time_range_view import DateTimeRangeView
from src.visualisation.base.date_time_range.date_time_range_view_model import DateTimeRangeViewModel


class DateTimeRangeViewFactory:
    """Creator of the DateTimeRangeView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> DateTimeRangeView:
        """creates a DateTimeRangeView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            DateTimeRangeView
        """
        view_model = DateTimeRangeViewModel(interpretation)

        if specification.is_request_for_preview:
            return DateTimeRangePreview(view_model)

        return DateTimeRangeView(view_model)
