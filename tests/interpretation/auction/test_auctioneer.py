# -*- coding: utf-8 -*-
import unittest

from doubles.double_dummy import Dummy
from doubles.type_system.double_info_bidder import InfoBidderMock
from doubles.interpretation.double_specification import SpecificationMock
from doubles.type_system.double_type_registry import TypeRegistryMock
from src.interpretation.auction.auctioneer import Auctioneer


class AuctioneerTestSuite(unittest.TestCase):
    def test_create_auctioneer(self):
        type_registry = Dummy('type_registry')
        Auctioneer(type_registry)

    def test_auction(self):
        factory1 = Dummy('InfoViewFactory1')
        bidder1 = InfoBidderMock(coverage=0.5, view_factory=factory1)
        factory2 = Dummy('InfoViewFactory2')
        bidder2 = InfoBidderMock(coverage=1, view_factory=factory2)
        type_registry = TypeRegistryMock([bidder1, bidder2])
        auctioneer = Auctioneer(type_registry)
        subject = Dummy('Info')
        specification = SpecificationMock()
        result = auctioneer.auction(subject, specification)
        self.assertNotIn(factory1, result)
        self.assertIn(factory2, result)

    def test_auction_with_no_fitting_offers(self):
        types = dict()
        type_registry = TypeRegistryMock(types)
        auctioneer = Auctioneer(type_registry)
        subject = Dummy('Info')
        specification = SpecificationMock()
        with self.assertRaises(
                KeyError,
                msg='Expected KeyError because no offers were provided'):
            auctioneer.auction(subject, specification)

    def test_only_satisfying_offers_are_considered(self):
        factory1 = Dummy('InfoViewFactory1')
        bidder1 = InfoBidderMock(satisfies=False, view_factory=factory1)
        factory2 = Dummy('InfoViewFactory2')
        bidder2 = InfoBidderMock(satisfies=True, view_factory=factory2)
        type_registry = TypeRegistryMock({bidder1: factory1, bidder2: factory2})
        auctioneer = Auctioneer(type_registry)
        subject = Dummy('Info')
        specification = SpecificationMock()
        result = auctioneer.auction(subject, specification)
        self.assertIn(factory2, result)
        self.assertNotIn(factory1, result)
