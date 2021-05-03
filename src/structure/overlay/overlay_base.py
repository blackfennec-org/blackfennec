class OverlayBase:
    def __init__(self, subject, overlay_factory):
        self._subject = subject
        self._overlay_factory = overlay_factory

    @property
    def subject(self):
        """Property for access on encapsulated info
            in this Overlay."""
        return self._subject

    @property
    def parent(self):
        """Property for parent of this info encapsulated
            in an Overlay."""
        return self._overlay_factory.create(self.subject.parent)

    @parent.setter
    def parent(self, parent: 'Info'):
        decapsulated_parent = self._remove_overlay_class(parent)
        self.subject.parent = decapsulated_parent

    @property
    def root(self):
        """Property for root of this info encapsulated in an Overlay."""
        return self._overlay_factory.create(self.subject.root)

    @staticmethod
    def _remove_overlay_class(value):
        decapsulated_value = value
        if isinstance(value, OverlayBase):
            subject: OverlayBase = value
            decapsulated_value = subject.subject
        return decapsulated_value
