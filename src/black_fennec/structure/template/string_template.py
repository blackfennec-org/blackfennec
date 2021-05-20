# -*- coding: utf-8 -*-
import logging
import re
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

    def visit_string(self, subject: String):
        """Check value of String for regexp

                Checks whether the value contained in the template
                    if any can be matched with the strings value.

                Args:
                    subject (List): String whose value has to match template
                    template (List): Template that may contains value which
                        if existing will be matched against the subjects value.

                Returns:
                    bool: Whether value of string matches regexp if any
                """
        subject_node_count, template_node_count = super().visit_string(subject)
        if self.value and self.value != '':
            if not re.match(self.value, subject.value):
                message = f'Pattern mismatch of subject({subject})' \
                          f' and pattern({self.value})'
                logger.info(message)
                template_node_count = 0
        return subject_node_count, template_node_count

    def __repr__(self):
        return f'StringTemplate({self.subject.__repr__()})'
