
class RootMock:
    def __init__(self):
        self.root = self
        self.parent = self

class InfoMock:
    def __init__(self):
        self.root = None
        self.parent = None