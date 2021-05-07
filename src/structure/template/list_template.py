# -*- coding: utf-8 -*-
import logging

from src.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.structure.list import List
from src.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class ListTemplate(ListEncapsulationBase, TemplateBase):
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