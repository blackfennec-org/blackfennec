import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec.interpretation.specification import Specification
from base.date_time.date_time_view_factory import DateTimeViewFactory

from base.date_time.date_time_preview import DateTimePreview


class DateTimeViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeViewFactory()

    def test_can_create_map_view(self):
        factory = DateTimeViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, DateTimePreview)

    def test_cannot_satisfy_view(self):
        factory = DateTimeViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertFalse(satisfies)

    def test_can_satisfy_preview(self):
        factory = DateTimeViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
