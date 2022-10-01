import unittest

from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from doubles.double_dummy import Dummy
from doubles.presentation.double_structure_presenter import StructurePresenterMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.navigation.navigation_service import NavigationService
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.visualisation.core.list.list_view_model import ListViewModel
from src.visualisation.core.map.map_view_model import MapViewModel
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.number_type import NumberType
from src.black_fennec.structure.type.reference_type import ReferenceType
from src.black_fennec.structure.type.string_type import StringType




class NavigationOnViewModelResultsInNavigationInPresenterTestSuite(
        unittest.TestCase):

    def setUp(self):
        type_registry = TypeRegistry()
        interpretation_service = InterpretationServiceMock([])
        template_registry = TemplateRegistryMock()
        type_registry.register_type(BooleanType())
        type_registry.register_type(NumberType())
        type_registry.register_type(StringType())
        type_registry.register_type(ListType())
        type_registry.register_type(MapType())
        self.presenter = StructurePresenterMock()
        self.navigation_service = NavigationService()
        self.navigation_service.set_presenter(self.presenter)

    def test_map_can_navigate(self):
        structure = Map()
        interpretation = Interpretation(
            structure, Dummy('specification'), Dummy('factories'))
        interpretation.set_navigation_service(self.navigation_service)
        interpretation_service = Dummy('InterpretationService')
        template_registry = TemplateRegistryMock()
        map_view_model = MapViewModel(
            interpretation,
            interpretation_service,
            template_registry)
        map_view_model.navigate_to(Map())
        self.assertEqual(self.presenter.show_count, 1)

    def test_list_can_navigate(self):
        structure = List()
        interpretation = Interpretation(
            structure, Dummy('specification'), Dummy('factories'))
        interpretation.set_navigation_service(self.navigation_service)
        interpretation_service = Dummy('InterpretationService')
        template_registry = Dummy('TemplateRegistry')
        list_view_model = ListViewModel(
            interpretation,
            interpretation_service,
            template_registry
        )
        list_view_model.navigate_to(List())
        self.assertEqual(self.presenter.show_count, 1)
