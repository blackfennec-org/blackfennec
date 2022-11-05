# -*- coding: utf-8 -*-

import logging

from blackfennec.interpretation.auction.coverage import Coverage
from blackfennec.structure.null import Null
from blackfennec.structure.map import Map
from blackfennec.type_system.type import Type
from blackfennec.structure.string import String

logger = logging.getLogger(__name__)


class NullType(Type):
    """Base Class for Type of a Null."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)

    @staticmethod
    def _type_structure():
        return Map({"type": String("Null"), "super": Null()})

    @property
    def default(self):
        return Null()

    def visit_null(self, subject: Null) -> Coverage:
        return Coverage.COVERED

    def __repr__(self):
        return f"NullType({self.subject.__repr__()})"
