import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_map import MapMock
from src.interpretation.specification import Specification
from src.type_system.base.address.address_view import AddressView
from src.type_system.base.address.address_view_factory import AddressViewFactory


class AddressViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressViewFactory()

    def test_can_create_map_view(self):
        factory = AddressViewFactory()
        view = factory.create(InterpretationMock(MapMock()), Specification())
        self.assertIsInstance(view, AddressView)

    def test_satisfies_default(self):
        factory = AddressViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = AddressViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
