import unittest

from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.base.person.person_view import PersonView
from src.visualisation.base.person.person_view_factory import PersonViewFactory


class PersonViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonViewFactory()

    def test_can_create_map_view(self):
        factory = PersonViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, PersonView)

    def test_satisfies_default(self):
        factory = PersonViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = PersonViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
