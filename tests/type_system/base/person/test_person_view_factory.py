import unittest

from doubles.structure.map import MapMock
from doubles.interpretation.interpretation import InterpretationMock
from src.type_system.base.person.person_view import PersonView
from src.type_system.base.person.person_view_factory import PersonViewFactory


class PersonViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonViewFactory()

    def test_can_create_map_view(self):
        factory = PersonViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, PersonView)
