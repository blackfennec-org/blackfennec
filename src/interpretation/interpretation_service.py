# -*- coding: utf-8 -*-
import logging

from src.structure.info import Info
from src.interpretation.auction.auctioneer import Auctioneer
from src.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


class InterpretationService:
    """Interpretation Service Class.

    Is produced during the selection process and is the
    Creator of Interpretations

    Attributes:
        _navigation_service (NavigationService): stores injected
            navigation service
        _auctioneer (Auctioneer): stores injected auctioneer
    """
    def __init__(self, auctioneer: Auctioneer):
        """Constructor of interpretation service

        Args:
            auctioneer (Auctioneer): selects the best offer based on the
                registered types.
        """
        self._auctioneer = auctioneer

    def interpret(self, structure: Info) -> Interpretation:
        """Interpret the given structure follwing the a specification

        Args:
            structure (Info): The structure to be interpreted
        Returns:
            Interpretation: Represents what black fennec believes to be
                the meaning of the structure.
        """
        interpretation = Interpretation(structure)
        factories = self._auctioneer.auction(structure)
        assert len(factories) == 1, 'cannot currently handle multiple factores'

        info_views = [ factories[0].create(interpretation) ]

        logger.debug(
            'creating interpretation of info %s with views %s',
            structure,
            info_views
        )
        interpretation.info_views = info_views
        return interpretation
