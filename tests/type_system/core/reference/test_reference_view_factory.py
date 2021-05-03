import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.structure.double_map import MapMock
from doubles.structure.double_reference import ReferenceInstanceMock
from src.interpretation.specification import Specification
from src.type_system.core.reference.reference_preview import ReferencePreview
from src.type_system.core.reference.reference_view_factory import ReferenceViewFactory


class ReferenceViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ReferenceViewFactory(InterpretationServiceMock([]))

    def test_can_create_reference_view(self):
        factory = ReferenceViewFactory(InterpretationServiceMock([]))
        with self.assertRaises(NotImplementedError):
            factory.create(InterpretationMock(MapMock()), Specification())

    def test_can_create_reference_preview(self):
        factory = ReferenceViewFactory(InterpretationServiceMock([]))
        view = factory.create(
            InterpretationMock(ReferenceInstanceMock()),
            Specification(request_preview=True)
        )
        self.assertIsInstance(view, ReferencePreview)

    def test_satisfies_default(self):
        factory = ReferenceViewFactory(InterpretationServiceMock([]))
        satisfies = factory.satisfies(Specification())
        self.assertFalse(satisfies)

    def test_does_satisfy_preview(self):
        factory = ReferenceViewFactory(InterpretationServiceMock([]))
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
