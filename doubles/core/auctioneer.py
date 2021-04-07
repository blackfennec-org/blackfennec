# -*- coding: utf-8 -*-
from doubles.dummy import Dummy


class AuctioneerMock:
    def __init__(self, factories=None):
        self._factories = [Dummy('InfoFactory')] if not factories else factories
        self.auction_count = 0
        self.auction_last_subject = None

    def auction(self, subject):
        self.auction_last_subject = subject
        self.auction_count += 1
        return self._factories
