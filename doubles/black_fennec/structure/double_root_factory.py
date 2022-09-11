# -*- coding: utf-8 -*-
import types

from src.black_fennec.structure.root_factory import RootFactory
from src.black_fennec.structure.structure import Structure


class RootFactoryMock(RootFactory):
    def __init__(self, root_getter=None, document_getter=None):
        self._root_getter = root_getter or (lambda: None)
        self._document_getter = document_getter or (lambda: None)
        self.make_root_structure_parameter = None
        self.make_root_document_parameter = None

    def make_root(self, structure: Structure, document=None):
        self.make_root_structure_parameter = structure
        self.make_root_document_parameter = document
