# -*- coding: utf-8 -*-
import logging
from blackfennec.structure.structure import Structure
from blackfennec.structure.reference_navigation.navigator import Navigator

logger = logging.getLogger(__name__)


class ParentNavigator(Navigator):
    def __init__(self):
        super().__init__()

    def navigate(self, current: Structure) -> Structure:
        """navigates current structure and returns destination

        Returns:
            Structure: Parent
        """
        return current.parent

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return ".."
