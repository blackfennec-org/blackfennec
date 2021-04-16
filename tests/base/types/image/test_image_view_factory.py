import unittest

from doubles.core import MapMock
from doubles.core.interpretation import InterpretationMock
from src.base.types.image.image_view import ImageView
from src.base.types.image.image_view_factory import ImageViewFactory


class ImageViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ImageViewFactory()

    def test_can_create_image_view(self):
        factory = ImageViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, ImageView)
