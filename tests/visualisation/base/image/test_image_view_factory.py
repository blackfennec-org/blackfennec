import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.base.image.image_view import ImageView
from src.visualisation.base.image.image_view_factory import ImageViewFactory


class ImageViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ImageViewFactory()

    def test_can_create_image_view(self):
        factory = ImageViewFactory()
        view = factory.create(InterpretationMock(MapMock()), Specification())
        self.assertIsInstance(view, ImageView)

    def test_satisfies_default(self):
        factory = ImageViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = ImageViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
