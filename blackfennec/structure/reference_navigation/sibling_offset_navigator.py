# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.list import List
from blackfennec.structure.structure import Structure
from blackfennec.structure.reference_navigation.navigator import Navigator

logger = logging.getLogger(__name__)


class SiblingOffsetNavigator(Navigator):
    def __init__(self, sibling_offset: int):
        super().__init__()
        self.sibling_offset: int = sibling_offset

    def navigate(self, current: Structure) -> Structure:
        """navigates current structure and returns destination

        Returns:
            Structure: Structure navigated to
        """
        parent = current.parent
        if not isinstance(parent, List):
            message = "Offset navigation can only be done on structures which parent is a list!"
            logger.error(message)
            raise ValueError(message)

        current_index = parent.value.index(current)
        destination_index = current_index + self.sibling_offset
        return parent.value[destination_index]

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f"sibling({self.sibling_offset})"

    def __eq__(self, other):
        if isinstance(other, SiblingOffsetNavigator):
            return self.sibling_offset == other.sibling_offset

    def __hash__(self):
        return hash(self.sibling_offset)
