# -*- coding: utf-8 -*-

import logging
import re

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.string import String
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class StringTemplate(TemplateBase):
    """Base Class for Template of a String."""

    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Map,
            is_optional: bool=False,
    ):
        TemplateBase.__init__(
            self,
            visitor,
            subject,
            is_optional
        )

    def create_instance(self):
        return self.default

    @property
    def default(self):
        if 'default' in self.subject.value:
            return String(self.subject.value['default'].value)
        return String('')

    @property
    def pattern(self) -> re.Pattern:
        if 'pattern' in self.subject.value:
            return re.compile(self.subject.value['pattern'].value)
        return re.compile('.*')

    def visit_string(self, subject: String) -> Coverage:
        """Check value of String for regexp

        Checks whether the value contained in the template
            if any can be matched with the strings value.

        Args:
            subject (List): String whose value has to match template
        Returns:
            Coverage: Coverage.COVERED if the match was successful
                or no regex was contained in the template value;
                Coverage.NOT_COVERED if the match failed.
        """
        coverage = Coverage.COVERED
        if not self.pattern.match(subject.value):
            message = f'Pattern mismatch of subject({subject})' \
                        f' and pattern({self.value})'
            logger.info(message)
            return Coverage.NOT_COVERED
        return coverage

    def __repr__(self):
        return f'StringTemplate({self.subject.__repr__()})'
