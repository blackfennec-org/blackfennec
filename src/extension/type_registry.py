class TypeRegistry:
    """Type Registry Class

    Is a register of all known or registered types.

    Attributes:
        _types: stores internal types
    """

    def __init__(self):
        """ type_registry constructor.

        Initializes the _types attribute with empty dictionary
        """
        self._types = dict()



    @property
    def types(self):
        """types getter

            Returns:
                dict: key type_bidder, value type_view_factory
        """
        return self._types


    def register_type(self, type_bidder, type_view_factory):
        """Function to register a new type

            Args:
                type_bidder (InfoBidder): key of the type dictionary
                type_view_factory (InfoViewFactory): value of the type
                    dictionary
        """
        self._types[type_bidder] = type_view_factory


    def deregister_type(self, type_bidder):
        """Function to deregister a type from the dictionary

        Args:
            type_bidder (InfoBidder): key of the type dictionary

        """
        self._types.pop(type_bidder)
