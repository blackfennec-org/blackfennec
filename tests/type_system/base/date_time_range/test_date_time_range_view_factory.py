import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.map import MapMock
from src.interpretation.specification import Specification
from src.type_system.base.date_time_range.date_time_range_view import DateTimeRangeView
from src.type_system.base.date_time_range.date_time_range_view_factory import DateTimeRangeViewFactory


class DateTimeRangeViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeRangeViewFactory()

    def test_can_create_map_view(self):
        factory = DateTimeRangeViewFactory()
        view = factory.create(InterpretationMock(MapMock()), Specification())
        self.assertIsInstance(view, DateTimeRangeView)

    def test_satisfies_default(self):
        factory = DateTimeRangeViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = DateTimeRangeViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
