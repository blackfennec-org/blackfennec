# -*- coding: utf-8 -*-
import logging
from typing import Union

from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.reference_navigation.navigator import Navigator

logger = logging.getLogger(__name__)


class ChildNavigator(Navigator):
    def __init__(self, token: str):
        super().__init__()
        self.subscript: str = token

    def navigate(self, current: Union[Map, List]) -> Structure:
        """navigates current structure and returns destination

        Returns:
            Structure: Structure navigated to
        """
        subscript: Union[str, int] = self.subscript
        if isinstance(current, List):
            subscript = int(subscript)

        current_value = current.value[subscript]
        return current_value

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return self.subscript

    def __eq__(self, other):
        if isinstance(other, ChildNavigator):
            return self.subscript == other.subscript

    def __hash__(self):
        return hash(self.subscript)
