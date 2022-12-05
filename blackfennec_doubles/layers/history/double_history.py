

class HistoryMock:
    def __init__(self) -> None:
        self.history = []
        self.undo_count = 0
        self.redo_count = 0

    def append(self, entry):
        self.history.append(entry)

    def can_undo(self):
        return len(self.history) > 0

    def can_redo(self):
        return len(self.history) > 0

    def undo(self):
        self.undo_count += 1

    def redo(self):
        self.redo_count += 1