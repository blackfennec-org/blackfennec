import unittest

from doubles.base.info_presenter import InfoPresenterMock
from src.core import NavigationService
from src.core import Auctioneer
from src.core.types.boolean.boolean_bidder import BooleanBidder
from src.core.types.list import List, ListViewModel
from src.core.types.list.list_bidder import ListBidder
from src.core.types.map import Map, MapViewModel
from src.core.types.map.map_bidder import MapBidder
from src.core.types.number.number_bidder import NumberBidder
from src.core.types.string.string_bidder import StringBidder
from src.core.interpretation import Interpretation
from src.extension.type_registry import TypeRegistry


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
