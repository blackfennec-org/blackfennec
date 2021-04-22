# -*- coding: utf-8 -*-

from src.type_system.base.image.image_view_model import ImageViewModel
from src.type_system.base.image.image_view import ImageView
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification


class ImageViewFactory:
    """Creator of the ImageView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
               _: Specification) -> ImageView:
        """creates a ImageView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            ImageView
        """
        view_model = ImageViewModel(interpretation)
        return ImageView(view_model)
