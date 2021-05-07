class OverlayFactoryMock:
    def __init__(self, create_return = None):
        self._subject = None
        self._property_storage = None
        self._create_calls = 0
        self._create_return = create_return

    def create(self, subject, property_storage: dict = None):
        self._create_calls += 1
        self._subject = subject
        self._property_storage = property_storage
        return self._create_return
