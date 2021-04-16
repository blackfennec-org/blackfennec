import unittest

from doubles.core import MapMock
from doubles.core.interpretation import InterpretationMock
from src.base.types.date_time.date_time_view import DateTimeView
from src.base.types.date_time.date_time_view_factory import DateTimeViewFactory


class DateTimeViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeViewFactory()

    def test_can_create_map_view(self):
        factory = DateTimeViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, DateTimeView)
