import logging
from src.black_fennec.structure.structure import Structure
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.interpretation.auction.offer import Offer

logger = logging.getLogger(__name__)


class Auctioneer:
    """A service to find the best offer, Auctioneer.

    Searches for the best offer provided by the types registered in
    the type registry. Only offers that satisfy the requested specification
    are considered. The sorting of offers is based on their implementation
    of the '>=' operator.
    """

    def __init__(self, type_registry):
        """Auctioneer constructor.

        Args:
            type_registry(TypeRegistry): source for known types. Only known
                types can be asked for an offer.
        """
        self._type_registry = type_registry

    def _select_offers(self,
                       subject: Structure,
                       bidders,
                       specification: Specification
    ) -> [Offer]:
        """Select the best offers.

        Args:
            subject (Structure): The subject to be auctioned off.
            bidders (StructureBidder): The bidders participating in the auction.
            specification (Specification): The specification which describes
                acceptable offers.

        Raises:
            KeyError: If no offer could be selected a key error is raised

        Returns:
            [Offer]: The best offers given a list of bidders.
        """
        best_offer = None

        for bidder in bidders:
            offer = bidder.bid(subject)

            if not offer.satisfies(specification):
                logger.debug('%s does not satisfy %s', offer, specification)
                continue

            if best_offer is None or offer >= best_offer:
                best_offer = offer

        if best_offer is None or not best_offer.coverage.is_covered():
            message = 'No offer is the best offer for subject({})'.format(
                str(subject)
            )
            logger.error(message)
            raise KeyError(message)
        return [best_offer]

    def auction(self, subject: Structure, specification: Specification) -> list:
        """Auction off a subject, using the specification when selecting offers.

        Auctions subject to all known types which can follow the specification.
            Each remaining type makes an offer communicating its suitability
            for handling the subject. The auctioneer selects the best offer.

        Args:
            subject (Structure): The subject (a.k.a structure)
                to be auctioned off.
            specification (Specification): The specification which must be
                upheld by bidders participating in the bidding.

        Raises:
            KeyError: If no factories could be selected a key error is raised

        Returns:
            [ViewFactory]: The factories which create views of the best types.
        """
        logger.debug('starting bidding on %s', subject)
        bidders = self._type_registry.types
        best_offers = self._select_offers(subject, bidders, specification)
        factories = list()
        for offer in best_offers:
            logger.debug(
                'adding view_factory of offer %s to factory list', offer)
            factories.append(offer.view_factory)
        return factories
