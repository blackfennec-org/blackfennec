# -*- coding: utf-8 -*-

from blackfennec.layers.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from .history_base import HistoryBase
from .history import History

class HistoryFactoryVisitor(BaseFactoryVisitor):
    def __init__(self, layer):
        BaseFactoryVisitor.__init__(self, layer, HistoryBase)