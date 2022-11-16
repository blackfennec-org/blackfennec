

class HistoryMock:
    def __init__(self) -> None:
        self.history = []

    def append(self, entry):
        self.history.append(entry)