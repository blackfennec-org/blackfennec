import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.map import MapMock
from src.type_system.base.date_time.date_time_view import DateTimeView
from src.type_system.base.date_time.date_time_view_factory import DateTimeViewFactory


class DateTimeViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeViewFactory()

    def test_can_create_map_view(self):
        factory = DateTimeViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, DateTimeView)
