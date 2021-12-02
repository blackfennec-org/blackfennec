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
        self._types = []

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
                type_bidder (StructureBidder): future element of the type list
        """
        self._types.append(type_bidder)

    def deregister_type(self, type_bidder_type: type):
        """Function to deregister a type from the dictionary if its class
            matches the passed type

        Args:
            type_bidder_type (type): element in the type list

        """
        for current_type in self._types:
            if current_type.__class__ == type_bidder_type:
                self._types.remove(current_type)
