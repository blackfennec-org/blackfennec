# -*- coding: utf-8 -*-
import logging

from src.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.structure.info import Info
from src.structure.list import List
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.reference import Reference

logger = logging.getLogger(__name__)


class ListOverlay(ListEncapsulationBase, OverlayBase):
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
        OverlayBase.__init__(
            self,
            visitor,
            subject
        )

    def __getitem__(self, index):
        item = self.subject[index]
        return self._encapsulate_and_dereference(item)

    def __repr__(self):
        return f'ListOverlay({self.subject.__repr__()})'