from doubles.type_system.info_bidder import InfoBidderMock
from doubles.type_system.info_view_factory import InfoViewFactoryMock


class TypeRegistryMock:

    def __init__(self, types=None):
        if type is None:
            self._types = dict()
            self._types[InfoBidderMock(1)] = InfoViewFactoryMock()
            self._types[InfoBidderMock(2)] = InfoViewFactoryMock()
        self._types = types
        self.types_getter_count = 0

        self.register_type_count = 0
        self.register_type_last_bidder = None
        self.register_type_last_view_factory = None

        self.deregister_type_count = 0
        self.deregister_type_last_bidder = None


    @property
    def types(self):
        self.types_getter_count += 1
        return self._types

    def register_type(self, type_bidder, type_view_factory):
        self.register_type_last_bidder = type_bidder
        self.register_type_last_view_factory = type_view_factory
        self.register_type_count += 1

    def deregister_type(self, type_bidder):
        self.deregister_type_last_bidder = type_bidder
        self.deregister_type_count += 1
