
class BlackFennecViewModel:
    def __init__(self, presenter):
        self._presenter = presenter

    @property
    def presenter(self):
        return self._presenter
