from .double_history import HistoryMock

class HistoryFactoryVisitorMock:
    def __init__(self, history=None):
        self.history = history or HistoryMock()