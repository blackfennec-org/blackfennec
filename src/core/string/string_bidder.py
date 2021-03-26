from src.core.info import Info
from src.core.string import String

class StringTypeBidder:
    """The bidding service for the core type `String`."""

    def bid(self, obj: Info):
        """"Produces an offer for a given object.

        Args:
            obj (:obj:`Info`): The Info for which an offer should be produced.
        """
        return isinstance(obj, String)
