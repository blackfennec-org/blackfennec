import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.base.date_time.date_time_view import DateTimeView
from src.visualisation.base.date_time.date_time_view_factory import DateTimeViewFactory

class DateTimeViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        DateTimeViewFactory()

    def test_can_create_map_view(self):
        factory = DateTimeViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, DateTimeView)

    def test_satisfies_default(self):
        factory = DateTimeViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = DateTimeViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
