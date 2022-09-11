# -*- coding: utf-8 -*-
import types

from src.black_fennec.structure.structure import Structure


class RootFactory:
    @staticmethod
    def make_root(structure: Structure, document=None):
        def root_getter(self):
            return structure

        def document_getter(self):
            return document

        structure.get_root = types.MethodType(root_getter, structure)
        structure.get_document = types.MethodType(document_getter, structure)
