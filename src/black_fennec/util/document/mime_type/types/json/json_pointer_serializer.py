# -*- coding: utf-8 -*-
import logging
import re

from src.black_fennec.structure.reference_navigation.child_navigator import ChildNavigator
from src.black_fennec.structure.reference_navigation.index_of_navigator import IndexOfNavigator
from src.black_fennec.structure.reference_navigation.navigator import Navigator
from src.black_fennec.structure.reference_navigation.parent_navigator import ParentNavigator
from src.black_fennec.structure.reference_navigation.root_navigator import RootNavigator
from src.black_fennec.structure.reference_navigation.sibling_offset_navigator import SiblingOffsetNavigator

logger = logging.getLogger(__name__)


class JsonPointerSerializer:
    """ JsonPointer Implementation according to RFC6901

        Class is able to serialize and deserialize JsonPointers in relative and
        absolute format.
    """
    ABSOLUTE_POINTER_PATTERN = \
        re.compile('^(/?(([^/~])|(~[01]))*)+$')
    RELATIVE_POINTER_PATTERN = \
        re.compile('^([0-9]+([+][0-9]+|[-][0-9]+)?)(/(([^/~])|(~[01]))*)*$')

    @staticmethod
    def serialize(navigator_list: list[Navigator]) -> str:
        """Serializes a list of navigators into a Json Pointer String

        Arguments:
            navigator_list (list[Navigator]): A list of navigators
        Returns:
            str: A Json Pointer String
        """
        reference = ""
        level_navigation = 0
        for navigator in navigator_list:
            if isinstance(navigator, ParentNavigator):
                level_navigation += 1
                navigator_list.remove(navigator)
            else:
                break

        if level_navigation:
            reference = str(level_navigation)

        first_element = navigator_list[0]
        if isinstance(first_element, SiblingOffsetNavigator):
            sibling_offset = first_element.sibling_offset
            if sibling_offset < 0:
                reference += "-"
            else:
                reference += "+"
            reference += str(sibling_offset)

        if reference:
            reference += "/"

        for navigator in navigator_list:
            if isinstance(navigator, ChildNavigator):
                reference += str(navigator.subscript) + "/"
            elif isinstance(navigator, IndexOfNavigator):
                reference += "#"

        return reference

    @classmethod
    def deserialize_absolute_pointer(cls, json_pointer: str) -> list[Navigator]:
        """Parses absolute JsonPointer.

        Returns:
            Navigator: Parsed absolute json pointer
        """
        token_list = cls._parse_token_list(json_pointer)

        navigator_list = [RootNavigator()]
        navigator_list += cls._deserialize_absolute_pointer(token_list)
        return navigator_list

    @classmethod
    def _deserialize_absolute_pointer(cls, token_list: [str]) -> list[Navigator]:
        """ Internal absolute JsonPointer parsing function
            expecting a navigator list

        Arguments:
             token_list ([str]): Navigator list
        Returns:
            list[Navigator]: parsed_pointer
        """
        token_list_index: int = 0 if token_list[0] else 1
        result_navigator_list: list[Navigator] = []
        while token_list_index < len(token_list):
            result_navigator_list.append(ChildNavigator(token_list[token_list_index]))
            token_list_index += 1
        return result_navigator_list

    @classmethod
    def deserialize_relative_pointer(cls, json_pointer: str) -> list[Navigator]:
        """ Deserialized relative JsonPointer.

        Arguments:
            json_pointer (str): Json pointer in string form
        Returns:
            Navigator: Parsed json pointer

        Raises:
            ValueError: if the first navigator in path did not match
                the expected format. [0-9]+([+-][0-9]+)?
        """
        token_list = cls._parse_token_list(json_pointer)
        get_key_of_value = False
        if str(token_list[-1]).endswith('#'):
            token_list[-1] = token_list[-1][:-1]
            get_key_of_value = True

        root_navigator: str = str(token_list[0])
        token_list[0] = None

        level_navigator, sibling_offset = cls._deserialize_root_navigator(root_navigator)

        result_navigator_list: list[Navigator] = []

        for i in range(int(level_navigator)):
            result_navigator_list.append(ParentNavigator())

        if sibling_offset:
            result_navigator_list.append(SiblingOffsetNavigator(sibling_offset))

        result_navigator_list += cls._deserialize_absolute_pointer(token_list)

        if get_key_of_value:
            result_navigator_list.append(IndexOfNavigator())
        return result_navigator_list

    @staticmethod
    def _remove_escaping_from_navigator(navigator):
        """Removes escaping from navigator

        Note that the order of escape resolvation
        is crucial. See [RFC6901] Section 4.

        Arguments:
            navigator (str): Represents on level of the JsonPointer
                that is inbetween two slashes.
        Returns:
            str: navigator with resolved escapings
        """
        navigator = navigator.replace('~1', '/')
        navigator = navigator.replace('~0', '~')
        return navigator

    @classmethod
    def _parse_token_list(cls, json_pointer: str):
        """ Takes JsonPointer in the form of a string.
            The function splits the received pointer by slashes and
            decodes the escapings '~0' -> '~' and '~1' -> '/'.

        Arguments:
            json_pointer (str): Json pointer string to deserialize

        Returns:
            [str]: Navigator list
        """
        hierarchy = json_pointer.split('/')
        token_list: [str] = []
        for navigator in hierarchy:
            token_list.append(
                cls._remove_escaping_from_navigator(navigator)
            )

        return token_list

    @staticmethod
    def _deserialize_root_navigator(root_navigator):
        """ Parses first navigator and extracts level navigator and sibling offset

        Arguments:
            root_navigator (str): token containing level navigator and index increment

        Returns:
             (int, int): Level navigator and index increment

        Raises:
            ValueError: If level navigator or sibling offset is not decimal
        """
        if '-' in root_navigator:
            offset_sign = -1
            offset_character = "-"
        elif '+' in root_navigator:
            offset_sign = 1
            offset_character = "+"

        else:
            if root_navigator.isdecimal():
                return int(root_navigator), 0
            else:
                message = f'Level navigator ({root_navigator}) is not decimal'
                logger.error(message)
                raise ValueError(message)

        split = root_navigator.split(offset_character)
        level_navigator = split[0]
        sibling_offset = split[1]
        if level_navigator.isdecimal() and sibling_offset.isdecimal():
            return level_navigator, int(sibling_offset) * offset_sign
        else:
            message = f'Level navigator ({level_navigator}) or sibling offset ({sibling_offset}) is not decimal'
            logger.error(message)
            raise ValueError(message)

    @staticmethod
    def is_relative_json_pointer(pointer: str):
        """ Checks if pointer is relative JsonPointer

        Arguments:
            pointer (str): JsonPointer string
        Returns:
            bool: True if pointer is relative JsonPointer
        """
        if JsonPointerSerializer.RELATIVE_POINTER_PATTERN.match(pointer):
            return True
        return False

    @staticmethod
    def is_absolute_json_pointer(pointer: str):
        """ Checks if pointer is absolute JsonPointer

        Arguments:
            pointer (str): JsonPointer string
        Returns:
            bool: True if pointer is absolute JsonPointer
        """
        if JsonPointerSerializer.ABSOLUTE_POINTER_PATTERN.match(pointer):
            return True
        return False
