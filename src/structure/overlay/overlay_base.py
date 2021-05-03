class OverlayBase:
    def __init__(self, subject, overlay_factory):
        self._subject = subject
        self._overlay_factory = overlay_factory

    @property
    def subject(self):
        """Property for access on encapsulated info in this OverlayAdapter."""
        return self._subject

    @property
    def parent(self):
        """Property for parent of this info encapsulated in an OverlayAdapter."""
        return self._overlay_factory.create(self.subject.parent)

    @property
    def root(self):
        """Property for root of this info encapsulated in an OverlayAdapter."""
        return self._overlay_factory.create(self.subject.root)