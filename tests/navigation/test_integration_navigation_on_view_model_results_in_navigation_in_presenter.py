import unittest

from doubles.presentation.info_presenter import InfoPresenterMock
from src.interpretation.auction.auctioneer import Auctioneer
from src.interpretation.interpretation import Interpretation
from src.navigation.navigation_service import NavigationService
from src.structure.list import List
from src.structure.map import Map
from src.type_system.core.boolean.boolean_bidder import BooleanBidder
from src.type_system.core.list.list_bidder import ListBidder
from src.type_system.core.list.list_view_model import ListViewModel
from src.type_system.core.map.map_bidder import MapBidder
from src.type_system.core.map.map_view_model import MapViewModel
from src.type_system.core.number.number_bidder import NumberBidder
from src.type_system.core.string.string_bidder import StringBidder
from src.type_system.type_registry import TypeRegistry


class NavigationOnViewModelResultsInNavigationInPresenterTestSuite(
        unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        registry.register_type(BooleanBidder())
        registry.register_type(NumberBidder())
        registry.register_type(StringBidder())
        registry.register_type(ListBidder())
        registry.register_type(MapBidder())
        self.presenter = InfoPresenterMock()
        auctioneer = Auctioneer(registry)
        self.navigation_service = NavigationService(self.presenter, auctioneer)

    def tearDown(self) -> None:
        self.registry = None
        self.auctioneer = None

    def test_map_can_navigate(self):
        info = Map()
        interpretation = Interpretation(self.navigation_service, info)
        map_view_model = MapViewModel(interpretation)
        map_view_model.navigate_to(Map())
        self.assertEqual(self.presenter.show_count, 1)

    def test_list_can_navigate(self):
        info = List()
        interpretation = Interpretation(self.navigation_service, info)
        list_view_model = ListViewModel(interpretation)
        list_view_model.navigate_to(List())
        self.assertEqual(self.presenter.show_count, 1)
