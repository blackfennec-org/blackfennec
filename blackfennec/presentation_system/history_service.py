from typing import Deque
from collections import deque
from blackfennec.structure.structure import Structure
from blackfennec.util.change_notification import ChangeNotification

from blackfennec.util.observable import Observable


class HistoryService:
    def __init__(self) -> None:
        self._history: Deque[HistoryEntry] = deque(maxlen=100)
        self._undone: Deque[HistoryEntry] = deque(maxlen=100)
        self._last_redone = None
        self._last_undone = None

    def observe(self, observable: Observable):
        observable.bind(changed=self._on_changed)

    def _on_changed(self, sender, notification: ChangeNotification):
        entry = HistoryEntry(
            sender,
            notification.old_value,
            notification.new_value)
        self._append(entry)

    def _append(self, entry: 'HistoryEntry'):
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

    def _is_last_undone(self, entry: 'HistoryEntry') -> bool:
        if self._last_undone is None:
            return False
        return self._last_undone.structure is entry.structure \
            and self._last_undone.old == entry.new \
            and self._last_undone.new == entry.old

    def _is_last_redone(self, entry: 'HistoryEntry') -> bool:
        if self._last_redone is None:
            return False
        return self._last_redone.structure is entry.structure \
            and self._last_redone.old == entry.old \
            and self._last_redone.new == entry.new


class HistoryEntry:
    def __init__(self, structure, old, new) -> None:
        self.structure: Structure = structure
        self.old = old
        self.new = new
