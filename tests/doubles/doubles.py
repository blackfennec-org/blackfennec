
class RootMock:
    def __init__(self):
        self.root = self
        self.parent = self

class InfoMock:
    def __init__(self):
        self.root = None
        self.parent = None

class InterprationMock:
    def __init__(self):
        self.navigation_requests = list()

    def navigate_to(self, info):
        self.navigation_requests.append(info)
