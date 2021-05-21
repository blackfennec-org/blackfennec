# -*- coding: utf-8 -*-
import logging
import re

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class StringTemplate(TemplateBase):
    """Base Class for Template of a String."""
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: String,
    ):
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

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
        if self.value and self.value != '':
            if not re.match(self.value, subject.value):
                message = f'Pattern mismatch of subject({subject})' \
                          f' and pattern({self.value})'
                logger.info(message)
                return Coverage.NOT_COVERED
        return coverage

    def __repr__(self):
        return f'StringTemplate({self.subject.__repr__()})'
