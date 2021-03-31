from src.core.info import Info
from src.core.interpreter import Interpreter
from src.core.offer import Offer


class Auctioneer:
    def __init__(self, type_registry):
        self._type_registry = type_registry

    def _select_offers(self, offers: [Offer]) -> [Offer]:
        offers: [Offer] = [max(offers)]
        assert offers, 'No type was found to handle info'
        return offers

    def auction(self, subject: Info, navigation_service):
        types = dict()
        for bidder, factory in self._type_registry.types.items():
            types[bidder.bid(subject)] = factory
        offers: [Offer] = self._select_offers(types.keys())
        factories = [types[key] for key in offers]
        return Interpreter(navigation_service, factories)
