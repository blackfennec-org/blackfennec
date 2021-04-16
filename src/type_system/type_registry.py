class TypeRegistry:
    """Type Registry Class

    Is a register of all known or registered types.

    Attributes:
        _types: stores internal types
    """

    def __init__(self):
        """ type_registry constructor.

        Initializes the _types attribute with empty list
        """
        self._types = list()

    @property
    def types(self):
        """types getter

            Returns:
                list: of type_bidder
        """
        return self._types

    def register_type(self, type_bidder):
        """Function to register a new type

            Args:
                type_bidder (InfoBidder): future element of the type list
        """
        self._types.append(type_bidder)

    def deregister_type(self, type_bidder):
        """Function to deregister a type from the dictionary

        Args:
            type_bidder (InfoBidder): element in the type list

        """
        self._types.remove(type_bidder)
