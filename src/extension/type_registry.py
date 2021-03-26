class TypeRegistry:

    def __init__(self):
        self._types = dict()

    @property
    def types(self):
        return self._types

    def register_type(self, type_bidder, type_view_factory):
        self._types[type_bidder] = type_view_factory

    def deregister_type(self, type_bidder):
        self._types.pop(type_bidder)
