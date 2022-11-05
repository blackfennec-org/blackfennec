# -*- coding: utf-8 -*-

import logging
import re

from blackfennec.interpretation.auction.coverage import Coverage
from blackfennec.structure.null import Null
from blackfennec.structure.string import String
from blackfennec.structure.map import Map

from .type import Type

logger = logging.getLogger(__name__)


class StringType(Type[String]):
    """Base Class for Type of a String."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)

    @staticmethod
    def _type_structure():
        return Map({"type": String("String"), "super": Null()})

    @property
    def pattern(self) -> re.Pattern:
        if "pattern" in self.subject.value:
            return re.compile(self.subject.value["pattern"].value)
        return re.compile(".*")

    def validate(self, subject):
        return self.pattern.match(subject.value)

    @property
    def default(self):
        if "default" in self.subject.value:
            return String(self.subject.value["default"].value)
        return String()

    def visit_string(self, subject: String) -> Coverage:
        """Check value of String for regexp

        Checks whether the value contained in the type
            if any can be matched with the strings value.

        Args:
            subject (List): String whose value has to match type
        Returns:
            Coverage: Coverage.COVERED if the match was successful
                or no regex was contained in the type value;
                Coverage.NOT_COVERED if the match failed.
        """
        coverage = Coverage.COVERED
        if not self.validate(subject):
            message = (
                f"Pattern mismatch of subject({subject}) "
                + f"and pattern({self.pattern})"
            )
            logger.info(message)
            return Coverage.NOT_COVERED
        return coverage

    def __repr__(self):
        return f"StringType({self.subject.__repr__()})"
