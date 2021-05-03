import unittest
from doubles.double_dummy import Dummy
from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_info import InfoMock
from doubles.structure.double_reference import ReferenceMock, ReferenceInstanceMock
from src.type_system.core.reference.reference_view_model import ReferenceViewModel


class ReferenceViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        interpretation = InterpretationMock(ReferenceInstanceMock())
        interpretation_service = Dummy('interpretation service')
        view_model = ReferenceViewModel(interpretation, interpretation_service)
        self.assertIsNotNone(view_model)

    def test_wrong_instance_in_interpretation(self):
        interpretation = InterpretationMock(ReferenceMock())
        interpretation_service = Dummy('interpretation service')
        with self.assertRaises(TypeError):
            ReferenceViewModel(interpretation, interpretation_service)

    def test_can_get_reference(self):
        reference = ReferenceInstanceMock()
        interpretation = InterpretationMock(reference)
        interpretation_service = Dummy('interpretation service')
        view_model = ReferenceViewModel(interpretation, interpretation_service)
        self.assertEqual(view_model.reference, reference)

    def test_can_forward_navigation_request(self):
        interpretation = InterpretationMock(ReferenceInstanceMock())
        interpretation_service = Dummy('interpretation service')
        view_model = ReferenceViewModel(interpretation, interpretation_service)
        route_target = InfoMock()
        view_model.navigate_to(route_target)
        self.assertListEqual(
            interpretation.navigation_requests,
            [route_target]
        )