# -*- coding: utf-8 -*-

from blackfennec.layers.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from .observable_base import ObservableBase


class ObservableFactoryVisitor(BaseFactoryVisitor):
    def __init__(self, layer):
        super().__init__(layer=layer, layer_base_class=ObservableBase)
