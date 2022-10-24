# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.string import String
from blackfennec.structure.structure import Structure
from blackfennec.structure.reference_navigation.navigator import Navigator

logger = logging.getLogger(__name__)


class IndexOfNavigator(Navigator):
    def navigate(self, current: Structure) -> Structure:
        """navigates to index/key of structure

        Returns:
            Structure: Structure navigated to
        """
        parent_structure = current.parent
        if isinstance(parent_structure, Map):
            parent_map: Map = parent_structure
            key_list = list(parent_map.value.keys())
            val_list = list(parent_map.value.values())

            position = val_list.index(current)
            result = String(key_list[position])
            result.parent = parent_structure
            return result
        elif isinstance(parent_structure, List):
            parent_list: List = parent_structure
            index = parent_list.value.index(current)
            result = Number(index)
            result.parent = parent_structure
            return result

        message = 'Cannot get key because parent is neither Map nor List'
        logger.error(message)
        raise TypeError(message)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return "#"
