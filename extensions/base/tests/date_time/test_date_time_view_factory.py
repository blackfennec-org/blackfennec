import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec.interpretation.specification import Specification
from base.date_time.date_time_view import DateTimeView
from base.date_time.date_time_view_factory import DateTimeViewFactory

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
