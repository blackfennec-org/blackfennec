# -*- coding: utf-8 -*-
import itertools
import re
import logging
from enum import Enum

from src.structure.info import Info
from src.structure.list import List
from src.structure.map import Map
from src.structure.string import String

logger = logging.getLogger(__name__)


class JsonPointerType(Enum):
    ABSOLUTE_JSON_POINTER = 0
    RELATIVE_JSON_POINTER = 1


class JsonPointer:
    ABSOLUTE_POINTER_PATTERN = re.compile('^((/?(([^/~])|(~[01]))*))+$')
    RELATIVE_POINTER_PATTERN = re.compile('^([0-9]+([+][0-9]+|[-][0-9]+)?)((/(([^/~])|(~[01]))*))+$')

    def __init__(self, json_pointer: str, json_pointer_type: JsonPointerType):
        self.path = (json_pointer, json_pointer_type)

    @property
    def path(self) -> [str]:
        return self._hierarchy

    @path.setter
    def path(self, value: (str, JsonPointerType)):
        pointer, pointer_type = value
        self._type = pointer_type
        hierarchy = pointer.split('/')
        self._hierarchy: [str] = list()
        for navigator in hierarchy:
            self._hierarchy.append(self._remove_escaping_from_navigator(navigator))

    @property
    def type(self) -> JsonPointerType:
        return self._type

    @staticmethod
    def _remove_escaping_from_navigator(navigator):
        """
        Note that the order of escape resolving
        is crucial. See [RFC6901] Section 4.

        :param navigator:
        :return:
        """
        navigator.replace('~1', '/')
        navigator.replace('~0', '~')
        return navigator

    @staticmethod
    def _navigate_in_list(source_list: List, navigator: str) -> Info:
        if navigator.isdecimal():
            list_index: int = int(navigator)
            if list_index < len(source_list.children):
                return source_list[list_index]
            else:
                message = 'Tried to access source_list(len={}) with index({}) ' \
                          'which is out of bounds'\
                    .format(
                        len(source_list), list_index
                    )
                logger.error(message)
                raise IndexError(message)
        else:
            message = 'Tried to access source_list with invalid ' \
                      'index({}) which is non-decimal and ' \
                      'thus invalid'.format(navigator),
            logger.error(message)
            raise ValueError(message)

    @staticmethod
    def _navigate_in_map(source_map: Map, navigator: str) -> Info:
        if navigator in source_map:
            return source_map[navigator]
        else:
            message = 'Key({}) could be found in map({})'.format(
                navigator,
                source_map
            )
            logger.error(message)
            raise KeyError(message)

    def resolve_absolute_pointer(self, source: Info):
        hierarchy_index: int = 0 if self._hierarchy[0] else 1
        current_location: Info = source
        while hierarchy_index < len(self._hierarchy):
            navigator: str = self._hierarchy[hierarchy_index]
            if isinstance(current_location, Map):
                current_location = self._navigate_in_map(current_location, navigator)
            elif isinstance(current_location, List):
                current_location = self._navigate_in_list(current_location, navigator)
            else:
                message = 'Navigator({}) could not be resolved on' \
                          'type {}'.format(navigator, type(current_location))
                logger.error(message)
                raise TypeError(message)
            hierarchy_index += 1
        assert hierarchy_index == len(self._hierarchy)
        return current_location

    def resolve_relative_pointer(self, source: Info):
        """Resolve relative json pointers

        Args:
            source (Info): Location from where to resolve pointer
        Returns:
            Info: Destination to which pointer points
        """
        current_location: Info = source
        level_navigator: str = self._hierarchy[0]
        self._hierarchy[0] = None

        index_increment = None
        if '-' in level_navigator:
            split = level_navigator.split('-')
            level_navigator = split[0]
            if split[1].isdecimal():
                index_increment = int(split[1]) * -1
            else:
                message = 'Array decrement({}) is not decimal'.format(
                    split[1])
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
            message = 'Level_navigator({}) is not decimal'.format(
                level_navigator)
            logger.error(message)
            raise ValueError(message)
        if index_increment:
            current_location = self._get_nth_next_sibling(current_location, index_increment)
        if self._hierarchy[-1].endswith('#'):
            return String(self._get_key_of_self(current_location))
        return self.resolve_absolute_pointer(current_location)

    @staticmethod
    def _get_key_of_self(child: Info) -> str:
        parent_info = child.parent
        if not isinstance(parent_info, Map):
            message = 'Cannot get key because parent is no Map'
            logger.error(message)
            raise TypeError(message)
        parent_map: Map = parent_info
        key_list = list(parent_map.keys())
        val_list = list(parent_map.values())

        position = val_list.index(child)
        return key_list[position]

    @staticmethod
    def _get_nth_next_sibling(child: Info, n: int):
        """
        Precondition: List shall not contain child multiple times

        Args:
            child (Info): child
            n (int): Index shift
        Returns:
            Info: sibling
        """
        parent_info = child.parent
        if not isinstance(parent_info, List):
            message = 'Cannot navigate because child is not in List'
            logger.error(message)
            raise TypeError(message)
        parent_list: List = parent_info
        index = parent_list.index(child)
        index += n
        return parent_list[index]

    def resolve_from(self, source: Info):
        if not source:
            message = 'No source passed to function ' \
                      'thus resolve of json_pointer impossible'
            logger.error(message)
            raise ValueError(message)
        if self.type == JsonPointerType.ABSOLUTE_JSON_POINTER:
            return self.resolve_absolute_pointer(source.root.child)
        elif self.type == JsonPointerType.RELATIVE_JSON_POINTER:
            return self.resolve_relative_pointer(source)
        message = 'Json Pointer type({}) not handled'.format(self.type.name)
        logger.error(message)
        raise ValueError(message)


def is_relative_json_pointer(pointer: str):
    if JsonPointer.RELATIVE_POINTER_PATTERN.match(pointer):
        return True
    return False
