# -*- coding: utf-8 -*-
import itertools
import re
import logging
from enum import Enum

from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String

logger = logging.getLogger(__name__)


class JsonPointerType(Enum):
    ABSOLUTE_JSON_POINTER = 0
    RELATIVE_JSON_POINTER = 1


class JsonPointer:
    """JsonPointer Implementation according to RFC6901

    Class is able to resolve JsonPointers in relative and
        absolute format on the black_fennec structure.
    """
    ABSOLUTE_POINTER_PATTERN = \
        re.compile('^(/?(([^/~])|(~[01]))*)+$')
    RELATIVE_POINTER_PATTERN = \
        re.compile('^([0-9]+([+][0-9]+|[-][0-9]+)?)(/(([^/~])|(~[01]))*)*$')

    def __init__(self, json_pointer: str, json_pointer_type: JsonPointerType):
        self.path = (json_pointer, json_pointer_type)

    @property
    def path(self) -> [str]:
        """Path setter

        Returns:
            [str]: the JsonPointer split by slashes whereas each
                item represents one hierarchy level. The first item
                might be empty because pointers with trailing slashes
                exist.
        """
        return self._hierarchy

    @path.setter
    def path(self, value: (str, JsonPointerType)):
        """

        Args:
            value (str, JsonPointerType): path setter takes JsonPointer
                in the form of a string accompanied by the type of the
                pointer in a tuple. The function splits the received pointer
                by slashes and decodes the escapings '~0' -> '~' and
                '~1' -> '/'.
        """
        pointer, pointer_type = value
        self._type = pointer_type
        hierarchy = pointer.split('/')
        self._hierarchy: [str] = []
        for navigator in hierarchy:
            self._hierarchy.append(
                self._remove_escaping_from_navigator(navigator)
            )

    @property
    def type(self) -> JsonPointerType:
        return self._type

    @staticmethod
    def _remove_escaping_from_navigator(navigator):
        """Removes escaping from navigator

        Note that the order of escape resolvation
        is crucial. See [RFC6901] Section 4.

        Args:
            navigator (str): Represents on level of the JsonPointer
                that is inbetween two slashes.
        Returns:
            str: navigator with resolved escapings
        """
        navigator.replace('~1', '/')
        navigator.replace('~0', '~')
        return navigator

    @staticmethod
    def _navigate_in_list(source_list: List, navigator: str) -> Structure:
        """Navigation in list(source_list) to index(navigator).

        Args:
            source_list (List): List of Structures
            navigator (str): Navigator to navigate in list. Expected to
                be the index that belongs to the item in the list

        Returns:
            Structure: which is identified through the index in the list
                that was passed as navigator

        Raises:
            IndexError: if the navigator(index) is out of bounds
            ValueError: if the navigator(index) is not decimal
        """
        if navigator.isdecimal():
            list_index: int = int(navigator)
            if list_index < len(source_list.value):
                return source_list.value[list_index]
            else:
                message = f'Tried to access source_list(' \
                          f'len={len(source_list.value)}) ' \
                          f'with index({list_index}) which is out of bounds'
                logger.error(message)
                raise IndexError(message)
        else:
            message = 'Tried to access source_list with invalid ' \
                      f'index({navigator}) which is non-decimal and ' \
                      'thus invalid'
            logger.error(message)
            raise ValueError(message)

    @staticmethod
    def _navigate_in_map(source_map: Map, navigator: str) -> Structure:
        """Navigation in Map(source_map) to key(navigator).

        Args:
            source_map (Map): Map of Structures
            navigator (str): Navigator to navigate in list. Expected to
                be the key that identifies the item in the Map

        Returns:
            Structure: which is identified through the key in the Map
                that was passed as navigator

        Raises:
            KeyError: if the navigator(key) does not exist in Map
        """
        if navigator in source_map.value:
            return source_map.value[navigator]
        else:
            message = 'Key({}) could be found in map({})'.format(
                navigator,
                source_map.value
            )
            logger.error(message)
            raise KeyError(message)

    def _resolve_absolute_pointer(self, source: Structure):
        """Resolve absolute JsonPointer.

        Args:
            source (Structure): Structure from which to navigate

        Returns:
            Structure: to which was navigated with the JsonPointer
                according to its path

        Raises:
            TypeError: if the JsonPointer could not be resolved
                properly, because the path did not correspond with
                the graph from the passed Structure
        """
        hierarchy_index: int = 0 if self._hierarchy[0] else 1
        current_location: Structure = source
        while hierarchy_index < len(self._hierarchy):
            navigator: str = self._hierarchy[hierarchy_index]
            if isinstance(current_location, Map):
                current_location = self._navigate_in_map(
                    current_location,
                    navigator
                )
            elif isinstance(current_location, List):
                current_location = self._navigate_in_list(
                    current_location,
                    navigator
                )
            else:
                message = f'Navigator({navigator}) could not be resolved on' \
                          f'type {type(current_location)}'
                logger.error(message)
                raise TypeError(message)
            hierarchy_index += 1
        assert hierarchy_index == len(self._hierarchy)
        return current_location

    def _resolve_relative_pointer(self, source: Structure):
        """Resolve relative JsonPointer.

        Resolves first navigator to find the starting point
            for the later resolving of the absolute pointer

        Args:
            source (Structure): Location from where to resolve pointer
        Returns:
            Structure: Destination to which pointer points

        Raises:
            ValueError: if the first navigator in path did not match
                the expected format. [0-9]+([+-][0-9]+)?
        """
        current_location: Structure = source

        get_key_of_value = False
        if str(self._hierarchy[-1]).endswith('#'):
            self._hierarchy[-1] = self._hierarchy[-1][:-1]
            get_key_of_value = True

        level_navigator: str = str(self._hierarchy[0])
        self._hierarchy[0] = None

        index_increment = None
        if '-' in level_navigator:
            split = level_navigator.split('-')
            level_navigator = split[0]
            if split[1].isdecimal():
                index_increment = int(split[1]) * -1
            else:
                message = f'Array decrement({split[1]}) is not decimal'
                logger.error(message)
                raise ValueError(message)
        elif '+' in level_navigator:
            split = level_navigator.split('+')
            level_navigator = split[0]
            if split[1].isdecimal():
                index_increment = int(split[1])
            else:
                message = 'Array increment({}) is not decimal'.format(
                    split[1])
                logger.error(message)
                raise ValueError(message)

        if level_navigator.isdecimal():
            for _ in itertools.repeat(None, int(level_navigator)):
                current_location = current_location.parent
        else:
            message = f'Level_navigator({level_navigator}) is not decimal'
            logger.error(message)
            raise ValueError(message)
        if index_increment:
            current_location = self._get_nth_next_sibling(
                current_location,
                index_increment
            )
        resolved = self._resolve_absolute_pointer(current_location)
        if get_key_of_value:
            return String(self._get_key_of_self(resolved))
        return resolved

    @staticmethod
    def _get_key_of_self(child: Structure) -> str:
        """Helper function to get Key of Map Item

        Args:
            child (Structure): for which the key should
                be searched

        Returns:
            str: Key of child that was passed

        Raises:
            TypeError: if the parent of the passed Structure is
                not of type Map
        """
        parent_structure = child.parent
        if not isinstance(parent_structure, Map):
            message = 'Cannot get key because parent is no Map'
            logger.error(message)
            raise TypeError(message)
        parent_map: Map = parent_structure
        key_list = list(parent_map.value.keys())
        val_list = list(parent_map.value.values())

        position = val_list.index(child)
        return key_list[position]

    @staticmethod
    def _get_nth_next_sibling(child: Structure, n: int):
        """
        Precondition: List shall not contain child multiple times

        Args:
            child (Structure): child
            n (int): Index shift
        Returns:
            Structure: sibling

        Raises:
            TypeError: if the parent of the passed Structure is
                not of type List
        """
        parent_structure = child.parent
        if not isinstance(parent_structure, List):
            message = 'Cannot navigate because child is not in List'
            logger.error(message)
            raise TypeError(message)
        parent_list: List = parent_structure
        index = parent_list.value.index(child)
        index += n
        return parent_list.value[index]

    def resolve_from(self, source: Structure):
        """Resolves JsonPointer from certain point.

        Returns:
            Structure: destination of JsonPointer.

        Raises:
            ValueError: if no source is passed to the function.
            NotImplementedError: if JsonPointerType of JsonPointer
                is not handled in this function.
        """
        if not source:
            message = 'No source passed to function ' \
                      'thus resolve of json_pointer impossible'
            logger.error(message)
            raise ValueError(message)
        if self.type == JsonPointerType.ABSOLUTE_JSON_POINTER:
            return self._resolve_absolute_pointer(source.get_root())
        elif self.type == JsonPointerType.RELATIVE_JSON_POINTER:
            return self._resolve_relative_pointer(source)
        message = f'Json Pointer type({self.type.name}) not handled'
        logger.error(message)
        raise NotImplementedError(message)


def is_relative_json_pointer(pointer: str):
    if JsonPointer.RELATIVE_POINTER_PATTERN.match(pointer):
        return True
    return False


def is_absolute_json_pointer(pointer: str):
    if JsonPointer.ABSOLUTE_POINTER_PATTERN.match(pointer):
        return True
    return False
