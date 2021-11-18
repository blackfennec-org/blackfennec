# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.list import List
from src.black_fennec.structure.filter.filter_base import FilterBase

logger = logging.getLogger(__name__)


class ListFilter(ListEncapsulationBase, FilterBase):
    """Base Class for Filters of a List."""

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
