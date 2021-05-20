# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class BooleanTemplate(TemplateBase):
    """Base Class for Template of a Boolean."""
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Boolean,
    ):
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

    def visit_boolean(self, subject: Boolean):
        return super().visit_boolean(subject)

    def __repr__(self):
        return f'BooleanTemplate({self.subject.__repr__()})'
