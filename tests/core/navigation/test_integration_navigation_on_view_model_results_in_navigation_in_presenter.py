import unittest

from doubles.base.info_presenter import InfoPresenterMock
from src.core import BooleanBidder, BooleanViewFactory, NumberBidder, NumberViewFactory, StringViewFactory, \
    StringBidder, ListBidder, ListViewFactory, MapBidder, MapViewFactory, Auctioneer, \
    NavigationService, Interpretation, MapViewModel, Map, List, ListViewModel
from src.extension.type_registry import TypeRegistry


class NavigationOnViewModelResultsInNavigationInPresenterTestSuite(unittest.TestCase):

    def setUp(self):
        registry = TypeRegistry()
        registry.register_type(BooleanBidder(), BooleanViewFactory())
        registry.register_type(NumberBidder(), NumberViewFactory())
        registry.register_type(StringBidder(), StringViewFactory())
        registry.register_type(ListBidder(), ListViewFactory())
        registry.register_type(MapBidder(), MapViewFactory())
        registry = registry
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






