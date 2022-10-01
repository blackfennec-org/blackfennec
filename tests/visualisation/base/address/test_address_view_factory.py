import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.base.address.address_view import AddressView
from src.visualisation.base.address.address_view_factory import AddressViewFactory


class AddressViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressViewFactory()

    def test_can_create_map_view(self):
        factory = AddressViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, AddressView)

    def test_satisfies_default(self):
        factory = AddressViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = AddressViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
