from src.core.string import String

class StringTypeBidder:
    def bid(self, obj):
        return isinstance(obj, String)
