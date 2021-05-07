# -*- coding: utf-8 -*-
import logging

from src.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.structure.list import List
from src.structure.filter.filter_base import FilterBase

logger = logging.getLogger(__name__)


class ListFilter(ListEncapsulationBase, FilterBase):
    def __init__(
            self,
            visitor: 'FilterFactoryVisitor',
            subject: List,
    ):
        ListEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        FilterBase.__init__(
            self,
            visitor,
            subject
        )

    def __repr__(self):
        return f'ListFilter({self.subject.__repr__()})'