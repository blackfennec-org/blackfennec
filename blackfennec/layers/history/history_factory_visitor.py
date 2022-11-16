# -*- coding: utf-8 -*-

from blackfennec.layers.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from .history_base import HistoryBase
from .history import History

class HistoryFactoryVisitor(BaseFactoryVisitor):
    def __init__(self, history: History):
        BaseFactoryVisitor.__init__(self, HistoryBase)
        self._history = history

    @property
    def history(self) -> History:
        return self._history
