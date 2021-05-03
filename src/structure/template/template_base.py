class TemplateBase:
    def __init__(
            self,
            subject,
            template_factory,
            property_storage: dict = None
    ):
        self._subject = subject
        self._property_storage = property_storage if property_storage \
            else dict()
        self._template_factory = template_factory

    @property
    def subject(self):
        """Property for access on encapsulated info in this OverlayAdapter."""
        return self._subject

    @property
    def optional(self):
        if self.subject in self._property_storage:
            return self._property_storage[self.subject]
        else:
            return False

    @optional.setter
    def optional(self, value: bool):
        self._property_storage[self.subject] = value

    @property
    def parent(self):
        """Property for parent of this info
            encapsulated in an OverlayAdapter."""
        return self._template_factory.create(
            self.subject.parent,
            self._property_storage
        )

    @parent.setter
    def parent(self, parent: 'Info'):
        decapsulated_parent = self._remove_template_class(parent)
        self.subject.parent = decapsulated_parent

    @property
    def root(self):
        """Property for root of this info encapsulated in an OverlayAdapter."""
        return self._template_factory.create(
            self.subject.root,
            self._property_storage
        )

    @staticmethod
    def _remove_template_class(value):
        decapsulated_value = value
        if isinstance(value, TemplateBase):
            subject: TemplateBase = value
            decapsulated_value = subject.subject
        return decapsulated_value
