# -*- coding: utf-8 -*-
import unittest

from doubles.base.info_presenter import InfoPresenterMock
from doubles.core.auctioneer import AuctioneerMock
from doubles.dummy import Dummy
from src.core.navigation.navigation_service import NavigationService


class NavigationServiceTestSuite(unittest.TestCase):
    def test_create_navigation_service(self):
        info_presenter = Dummy('InfoPresenter')
        auctioneer = Dummy('Auctioneer')
        NavigationService(info_presenter, auctioneer)

    def test_navigate(self):
        sender = Dummy('Interpretation')
        destination = Dummy('Info')
        type_registry = Dummy('TypeRegistry')
        auctioneer = AuctioneerMock(type_registry)
        info_presenter = InfoPresenterMock()
        navigation_service = NavigationService(info_presenter, auctioneer)
        navigation_service.navigate(sender, destination)
        self.assertEqual(
            auctioneer.auction_count,
            1
        )
        self.assertEqual(
            auctioneer.auction_last_subject,
            destination
        )
        self.assertEqual(
            info_presenter.show_count,
            1
        )
        self.assertEqual(
            info_presenter.show_last_sender,
            sender
        )
        self.assertEqual(
            info_presenter.show_last_destination,
            destination
        )
