from src.black_fennec.structure.type.type import Type


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
        return list(self._types)

    def register_type(self, type: Type):
        """Function to register a new type

            Args:
                type_bidder (StructureBidder): future element of the type list
        """
        self._types.append(type)

    def deregister_type(self, type: Type):
        """Function to deregister a type from the dictionary if its class
            matches the passed type

        Args:
            type (Type): element in the type list

        """
        assert type in self._types

        self._types.remove(type)
