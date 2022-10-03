# -*- coding: utf-8 -*-

import logging

from typing import Optional
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.type.type import Type
from src.black_fennec.structure.string import String

logger = logging.getLogger(__name__)


class BooleanType(Type):
    """Base Class for Type of a Boolean."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)

    @staticmethod
    def _type_structure():
        return Map({"type": String("Boolean"), "super": Null()})

    @property
    def default(self):
        if "default" in self.subject.value:
            return Boolean(self.subject.value["default"].value)
        return Boolean()

    @property
    def expected(self) -> Optional[bool]:
        if "expected" in self.subject.value:
            return self.subject.value["expected"].value
        return None

    @expected.setter
    def expected(self, value):
        if self.expected == None:
            self.subject.remove_item("expected")
            self.subject.add_item("expected", Boolean())
        self.subject.value["expected"].value = value

    def visit_boolean(self, subject: Boolean) -> Coverage:
        if self.expected != None and subject.value != self.expected:
            return Coverage.NOT_COVERED
        return Coverage.COVERED

    def __repr__(self):
        return f"BooleanType({self.subject.__repr__()})"
