from doubles.dummy import Dummy
from src.core.info import Info
from src.core.interpreter import Interpreter
from src.core.auction.offer import Offer


class Auctioneer:
    """Auctioneer Class.

    Decides how Info is interpreted and creates
    and Interpreter with the most suitable type

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

    def _select_offers(self, offers: [Offer]) -> [Offer]:
        """Offer selection.

        Gets a list of Offers and selects the most suitable
        Can be multiple.

        Args:
            offers([Offer]): list of offers to choose from

        Returns:
            [Offer]: most suitable offers
        """
        return [max(offers)]

    def auction(self, subject: Info) -> Interpreter:
        """Auction of Info.

        Auctions subject to all know types and each
        type can make an offer of how capable he is
        in handling the subject

        Args:
            subject(Info): Info to auction

        Returns:
            Interpreter: Interpreter capable of creating
                an interpretation of the type
        """
        types = dict()
        for bidder, factory in self._type_registry.types.items():
            types[bidder.bid(subject)] = factory
        offers: [Offer] = self._select_offers(types.keys())
        factories = [types[key] for key in offers]
        return Interpreter(Dummy("nav"), factories)
