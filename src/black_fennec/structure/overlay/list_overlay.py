# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.list import List
from src.black_fennec.structure.overlay.overlay_base import OverlayBase

logger = logging.getLogger(__name__)


class ListOverlay(ListEncapsulationBase, OverlayBase):
    """Base Class for Overlay of a List."""
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
