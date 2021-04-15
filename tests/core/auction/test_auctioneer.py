# -*- coding: utf-8 -*-
import unittest

from doubles.core.types.info_bidder import InfoBidderMock
from doubles.dummy import Dummy
from doubles.extension.type_registry import TypeRegistryMock
from src.core.auction.auctioneer import Auctioneer


class AuctioneerTestSuite(unittest.TestCase):
    def test_create_auctioneer(self):
        type_registry = Dummy('type_registry')
        Auctioneer(type_registry)

    def test_auction(self):
        types = dict()
        bidder1 = InfoBidderMock(1)
        bidder2 = InfoBidderMock(2)
        types[bidder1] = Dummy('InfoViewFactory1')
        types[bidder2] = Dummy('InfoViewFactory2')
        type_registry = TypeRegistryMock(types)
        auctioneer = Auctioneer(type_registry)
        subject = Dummy('Info')
        auctioneer.auction(subject)
        self.assertEqual(bidder1.bid_count, 1)
        self.assertEqual(bidder1.last_bidding_subject, subject)
        self.assertEqual(bidder2.bid_count, 1)
        self.assertEqual(bidder2.last_bidding_subject, subject)

    def test_auction_no_offers_fitting(self):
        types = dict()
        type_registry = TypeRegistryMock(types)
        auctioneer = Auctioneer(type_registry)
        subject = Dummy('Info')
        with self.assertRaises(
                KeyError,
                msg='Expected KeyError because no offers were provided'
        ):
            auctioneer.auction(subject)
