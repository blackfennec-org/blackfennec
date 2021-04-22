import unittest

from doubles.structure.map import MapMock
from doubles.interpretation.interpretation import InterpretationMock
from src.interpretation.specification import Specification
from src.type_system.base.person.person_view import PersonView
from src.type_system.base.person.person_view_factory import PersonViewFactory


class PersonViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonViewFactory()

    def test_can_create_map_view(self):
        factory = PersonViewFactory()
        view = factory.create(InterpretationMock(MapMock()), Specification())
        self.assertIsInstance(view, PersonView)

    def test_satisfies_default(self):
        factory = PersonViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = PersonViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
