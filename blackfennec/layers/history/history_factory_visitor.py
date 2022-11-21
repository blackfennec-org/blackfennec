# -*- coding: utf-8 -*-

from blackfennec.layers.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from .history_base import HistoryBase
from .history import History

class HistoryFactoryVisitor(BaseFactoryVisitor):
    def __init__(self, layer):
        super().__init__(layer=layer, layer_base_class=HistoryBase)