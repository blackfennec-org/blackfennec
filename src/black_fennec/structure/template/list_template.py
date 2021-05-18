# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.list import List
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class ListTemplate(ListEncapsulationBase, TemplateBase):
    """Base Class for Template of a List."""
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: List,
    ):
        ListEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

    def __repr__(self):
        return f'ListTemplate({self.subject.__repr__()})'
