import unittest

from doubles.core import MapMock
from doubles.core.interpretation import InterpretationMock
from src.base.types.person.person_view import PersonView
from src.base.types.person.person_view_factory import PersonViewFactory


class PersonViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonViewFactory()

    def test_can_create_map_view(self):
        factory = PersonViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, PersonView)
