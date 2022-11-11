# -*- coding: utf-8 -*-
import types

from blackfennec.structure.structure import Structure


class RootFactory:
    @staticmethod
    def make_root(structure: Structure, document=None):
        def document_getter(self):
            return document
        structure.get_document = types.MethodType(document_getter, structure)
