from src.core.info import Info
from src.core.interpreter import Interpreter
from src.core.auction.offer import Offer


class Auctioneer:
    """Auctioneer Class.

    Decides how Info is interpreted and creates
    an Interpreter with the most suitable type

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

        Gets a list of Offers and selects the most suitable.
        Can be multiple.

        Args:
            offers([Offer]): list of offers to choose from

        Returns:
            [Offer]: most suitable offers
        """
        offers: [Offer] = [max(offers)]
        assert offers, 'No type was found to handle info'
        return offers

    def auction(self, subject: Info, navigation_service):
        """Auction of Info.

        Auctions subject to all know types and each
        type can make an offer of how capable he is
        in handling the subject

        Args:
            subject(Info): Info to auction
            navigation_service(NavigationService): Navigation service
                required for passing to interpretation

        Returns:
            Interpreter: Interpreter capable of creating
                an interpretation of the type
        """
        types = dict()
        for bidder, factory in self._type_registry.types.items():
            types[bidder.bid(subject)] = factory
        offers: [Offer] = self._select_offers(types.keys())
        factories = [types[key] for key in offers]
        return Interpreter(navigation_service, factories)
