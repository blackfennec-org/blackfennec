from collections import deque
from .history_entry import HistoryEntry

class History:
    def __init__(self) -> None:
        self._history = deque(maxlen=100)
        self._undone = deque(maxlen=100)
        self._last_redone = None
        self._last_undone = None

    def append(self, entry: HistoryEntry):
        if self._is_last_undone(entry):
            return
        self._history.append(entry)
        if self._is_last_redone(entry):
            return
        self._undone.clear()

    def can_undo(self):
        return len(self._history) > 0

    def undo(self):
        entry = self._history.pop()
        self._undone.append(entry)
        self._last_undone = entry
        entry.structure.value = entry.old

    def can_redo(self):
        return len(self._undone) > 0

    def redo(self):
        entry = self._undone.pop()
        self._last_redone = entry
        entry.structure.value = entry.new

    def _is_last_undone(self, entry) -> bool:
        if self._last_undone is None:
            return False
        return self._last_undone.structure is entry.structure \
            and self._last_undone.old == entry.new \
            and self._last_undone.new == entry.old

    def _is_last_redone(self, entry) -> bool:
        if self._last_redone is None:
            return False
        return self._last_redone.structure is entry.structure \
            and self._last_redone.old == entry.old \
            and self._last_redone.new == entry.new
