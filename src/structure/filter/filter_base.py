class FilterBase:
    def __init__(
            self,
            subject,
            filter_factory,
            property_storage: dict = None
    ):
        self._subject = subject
        self._property_storage = property_storage if property_storage \
            else dict()
        self._filter_factory = filter_factory

    @property
    def subject(self):
        """Property for access on encapsulated info in this Filter."""
        return self._subject

    @property
    def filter(self):
        if self.subject in self._property_storage:
            return self._property_storage[self.subject]
        else:
            return False

    @filter.setter
    def filter(self, value: bool):
        self._property_storage[self.subject] = value

    @property
    def parent(self):
        """Property for parent of this info
            encapsulated in a Filter."""
        return self._filter_factory.create(
            self.subject.parent,
            self._property_storage
        )

    @parent.setter
    def parent(self, parent: 'Info'):
        decapsulated_parent = self._remove_filter_class(parent)
        self.subject.parent = decapsulated_parent

    @property
    def root(self):
        """Property for root of this info encapsulated in a filter."""
        return self._filter_factory.create(
            self.subject.root,
            self._property_storage
        )

    @staticmethod
    def _remove_filter_class(value):
        decapsulated_value = value
        if isinstance(value, FilterBase):
            subject: FilterBase = value
            decapsulated_value = subject.subject
        return decapsulated_value
