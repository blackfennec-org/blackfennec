# -*- coding: utf-8 -*-

import logging

from typing import Optional
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.template import Template

logger = logging.getLogger(__name__)


class BooleanTemplate(Template):
    """Base Class for Template of a Boolean."""

    def __init__(self, visitor: "TemplateParser", subject: Map):
        Template.__init__(self, visitor, subject)

    @property
    def default(self):
        if "default" in self.subject.value:
            return Boolean(self.subject.value["default"].value)
        return Boolean()

    @property
    def expected(self) -> Optional[bool]:
        if 'expected' in self.subject.value:
            return self.subject.value['expected'].value
        return None

    @expected.setter
    def expected(self, value):
        if self.expected == None:
            self.subject.remove_item('expected')
            self.subject.add_item('expected', Boolean())
        self.subject.value['expected'].value = value


    def visit_boolean(self, subject: Boolean) -> Coverage:
        if self.expected != None and subject.value != self.expected:
            return Coverage.NOT_COVERED
        return Coverage.COVERED

    def __repr__(self):
        return f"BooleanTemplate({self.subject.__repr__()})"
