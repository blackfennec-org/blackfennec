import unittest
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_reference import ReferenceMock, ReferenceInstanceMock
from src.visualisation.core.reference.reference_view_model import ReferenceViewModel


class ReferenceViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        interpretation = InterpretationMock(ReferenceInstanceMock())
        view_model = ReferenceViewModel(interpretation)
        self.assertIsNotNone(view_model)

    def test_wrong_instance_in_interpretation(self):
        interpretation = InterpretationMock(ReferenceMock())
        with self.assertRaises(TypeError):
            ReferenceViewModel(interpretation)

    def test_can_get_reference(self):
        reference = ReferenceInstanceMock()
        interpretation = InterpretationMock(reference)
        view_model = ReferenceViewModel(interpretation)
        self.assertEqual(view_model.reference, reference)

    def test_can_forward_navigation_request(self):
        interpretation = InterpretationMock(ReferenceInstanceMock())
        view_model = ReferenceViewModel(interpretation)
        route_target = StructureMock()
        view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target]
        )
