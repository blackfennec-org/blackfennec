class InterprationMock:
    def __init__(self):
        self.navigation_requests = list()

    def navigate_to(self, info):
        self.navigation_requests.append(info)
