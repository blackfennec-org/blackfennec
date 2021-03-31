# -*- coding: utf-8 -*-

class AuctioneerMock:
    def __init__(self, type_registry):
        self.type_registry = type_registry
        self.auction_count = 0
        self.auction_last_subject = None

    def auction(self, subject, navigation_service):
        self.auction_last_subject = subject
        self.auction_last_navigation_service = navigation_service
        self.auction_count += 1
