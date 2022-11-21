from .history_factory_visitor import HistoryFactoryVisitor
from .history import History

class RecordingLayer:
    def __init__(self, history):
        self._factory = HistoryFactoryVisitor(self)
        self._layer = {}
        self._history = history

    def apply(self, structure):
        if structure in self._layer:
            return self._layer[structure]
        encap = structure.accept(self._factory)
        self._layer[structure] = encap
        return encap
    

    @property
    def history(self) -> History:
        return self._history
