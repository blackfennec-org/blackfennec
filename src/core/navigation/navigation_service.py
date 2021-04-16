# -*- coding: utf-8 -*-
from src.core.auction.auctioneer import Auctioneer
from src.core.types.info import Info
from src.core.interpretation import Interpretation
from src.core.interpretation_service import InterpretationService


class NavigationService:
    """Navigation Service Class.

    Can be called by an interpretation for navigational purposes.
    Class resolves route through auctioneer and dispatches navigation
    request to info presenter.

    Attributes:
        _info_presenter (InfoPresenter): stores injected
            info presenter
        _auctioneer (Auctioneer): stores injected auctioneer
    """
    def __init__(self, info_presenter, auctioneer: Auctioneer):
        """Navigation Service constructor.

        Args:
            info_presenter (InfoPresenter): info presenter to show navigation
            auctioneer (Auctioneer): Auctioneer for type resolving
        """
        self._info_presenter = info_presenter
        self._auctioneer = auctioneer

    def navigate(self, sender: Interpretation, destination: Info):
        """Navigation request dispatch

        Dispatches navigation request received by Interpretation
        to column_based_presenter to show navigation with the help
        of the received interpretation_service

        Args:
            sender (Interpretation) Interpretation which invoked navigation
            destination (Info): Destination to which shall be navigated
        """
        interpreter = InterpretationService(self, self._auctioneer)
        self._info_presenter.show(sender, destination, interpreter)
