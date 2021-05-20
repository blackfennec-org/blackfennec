class Comparable:
    """Comparable mixin

    Only two comparison operators have to be implemented(eq,lt)
    and the rest can be included via this class."""

    def __ne__(self, other: 'Comparable') -> bool:
        return not self == other

    def __le__(self, other: 'Comparable') -> bool:
        return self == other or self < other

    def __gt__(self, other: 'Comparable') -> bool:
        return not self <= other

    def __ge__(self, other: 'Comparable') -> bool:
        return not self < other
