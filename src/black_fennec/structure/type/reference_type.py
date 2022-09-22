# -*- coding: utf-8 -*-

import logging

from typing import Optional
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.type.type import Type
from src.black_fennec.structure.string import String

logger = logging.getLogger(__name__)


class ReferenceType(Type):
    """Base Class for Type of a Boolean."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)

    @staticmethod
    def _type_structure():
        return Map({"type": String("Reference")})

    @property
    def default(self):
        if "default" in self.subject.value:
            return Reference(self.subject.value["default"].value)
        return Reference(None)

    def visit_reference(self, subject: Reference) -> Coverage:
        return Coverage.COVERED

    def __repr__(self):
        return f"ReferenceType({self.subject.__repr__()})"
