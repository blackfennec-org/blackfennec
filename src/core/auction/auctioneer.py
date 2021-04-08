import logging
from src.core.info import Info
from src.core.auction.offer import Offer

logger = logging.getLogger(__name__)
class Auctioneer:
    """Auctioneer Class.

    Decides how Info is interpreted and creates
    an list of factories of the most suitable type

    Attributes:
        _type_registry (TypeRegistry): stores injected
            type registry
    """
    def __init__(self, type_registry):
        """Auctioneer constructor.

        Args:
            type_registry(TypeRegistry): type registry to
                retrieve registered types from.
        """
        self._type_registry = type_registry

    def _select_offers(self, subject, offers: [Offer]) -> [Offer]:
        """Offer selection.

        Gets a list of Offers and selects the most suitable.
        Can be multiple.

        Args:
            offers([Offer]): list of offers to choose from

        Returns:
            [Offer]: most suitable offers
        """
        if offers:
            best_offer = offers[0]
        selection = False
        for offer in offers:
            if offer > best_offer:
                best_offer = offer
                selection = True
        if not selection:
            message = 'No offer is the best offer'
            logger.error(message)
            raise KeyError(message)
        return [best_offer]

    def auction(self, subject: Info):
        """Auction of Info.

        Auctions subject to all know types and each
        type can make an offer of how capable he is
        in handling the subject

        Args:
            subject(Info): Info to auction

        Returns:
            [InfoFactory]: Factories selected according to
                selected offers
        """
        logger.debug('starting bidding on %s', subject)
        offers = list()
        for bidder in self._type_registry.types:
            offers.append(bidder.bid(subject))
        best_offers = self._select_offers(subject, offers)
        factories = list()
        for offer in best_offers:
            logger.debug('adding view_factory of offer %s to factory list', offer)
            factories.append(offer.view_factory)
        return factories
