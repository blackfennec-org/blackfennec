# -*- coding: utf-8 -*-
from src.visualisation.base.image.image_preview import ImagePreview
from src.visualisation.base.image.image_view_model import ImageViewModel
from src.visualisation.base.image.image_view import ImageView
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class ImageViewFactory:
    """Creator of the ImageView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> ImageView:
        """creates a ImageView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            ImageView
        """
        view_model = ImageViewModel(interpretation)

        if specification.is_request_for_preview:
            return ImagePreview(view_model)

        return ImageView(view_model)
