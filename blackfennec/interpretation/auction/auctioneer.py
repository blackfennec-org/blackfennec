import logging
from blackfennec.structure.structure import Structure
from blackfennec.type_system.type import Type
from blackfennec.interpretation.auction.offer import Offer

logger = logging.getLogger(__name__)


class Auctioneer:
    """A service to find the best offer, Auctioneer.

    Searches for the best offer provided by the types registered in
    the type registry. Only offers that satisfy the requested specification
    are considered. The sorting of offers is based on their implementation
    of the '>=' operator.
    """

    @classmethod
    def _filter_offers(cls, subject: Structure, offers) -> list[Offer]:
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

        for offer in offers:
            logger.debug("checking offer %s", offer)
            logger.debug("offer is covered = %s", offer.coverage.is_covered())

            if best_offer is None or offer >= best_offer:
                best_offer = offer

        if best_offer is None or not best_offer.coverage.is_covered():
            message = f"No offer is the best offer for subject({str(subject)})"
            logger.error(message)
            raise KeyError(message)
        return [best_offer]

    @classmethod
    def auction(cls, types: list[Type], subject: Structure) -> list[Type]:
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
        logger.debug("starting bidding on %s", subject)
        offers = (Offer(subject, type) for type in types)
        best_offers = cls._filter_offers(subject, offers)
        types = []
        for offer in best_offers:
            logger.debug("adding types of offer %s to factory list", offer)
            types.append(offer.type)
        return types
