# -*- coding: utf-8 -*-

from src.base.types.image.image_view_model import ImageViewModel
from src.base.types.image.image_view import ImageView


class ImageViewFactory:
    """Creator of the ImageView"""

    def create(self, interpretation) -> ImageView:
        """creates a ImageView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            ImageView
        """
        view_model = ImageViewModel(interpretation)
        return ImageView(view_model)
