# -*- coding: utf-8 -*-
from doubles.interpretation.auction.offer import OfferFake


class InfoBidderMock:
    def __init__(self, value):
        self._offer = OfferFake(value)
        self.bid_count = 0
        self.last_bidding_subject = None

    def bid(self, subject):
        self.last_bidding_subject = subject
        self.bid_count += 1
        return self._offer
