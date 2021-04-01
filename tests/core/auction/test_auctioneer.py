# -*- coding: utf-8 -*-
import unittest

from doubles.core.info_bidder import InfoBidderMock
from doubles.dummy import Dummy
from doubles.extension.type_registry import TypeRegistryMock
from src.core.auction.auctioneer import Auctioneer
from src.core.interpreter import Interpreter


class InterpretationTestSuite(unittest.TestCase):
    def test_create_auctioneer(self):
        type_registry = Dummy('type_registry')
        Auctioneer(type_registry)

    def test_auction(self):
        types = dict()
        bidder1 = InfoBidderMock(1)
        bidder2 = InfoBidderMock(2)
        types[bidder1] = Dummy('factory1')
        types[bidder2] = Dummy('factory2')
        type_registry = TypeRegistryMock(types)
        auctioneer = Auctioneer(type_registry)
        subject = Dummy('subject')
        interpreter = auctioneer.auction(subject)
        self.assertIsInstance(interpreter, Interpreter)
        self.assertEqual(bidder1.bid_count, 1)
        self.assertEqual(bidder1.last_bidding_subject, subject)
        self.assertEqual(bidder2.bid_count, 1)
        self.assertEqual(bidder2.last_bidding_subject, subject)
