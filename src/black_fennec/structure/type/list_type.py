# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String
from .type import Type


logger = logging.getLogger(__name__)


class ListType(Type[List]):
    """Base Class for Type of a List."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)

    @staticmethod
    def _type_structure():
        return Map({"type": String("List"), "super": Null()})

    @property
    def default(self):
        return List([type.create_instance() for type in self.elements])

    @property
    def _elements(self):
        if "elements" not in self.subject.value:
            self.subject.add_item("elements", List())
        return self.subject.value["elements"]

    def add_element(self, type, is_required=True) -> None:
        self._elements.add_item(type.subject)
        if is_required:
            self.set_is_child_optional(type, not is_required)

    def _is_element_guard(self, index):
        if index < 0 or index >= len(self.elements):
            raise AssertionError(f"index:{index} out of range")

    @property
    def elements(self) -> list[Type]:
        raw_elements = self._elements.value

        elements = []
        for element in raw_elements:
            from .type_parser import TypeParser
            type = TypeParser.parse(element)
            elements.append(type)

        return elements

    @property
    def required_elements(self) -> list[str]:
        return self._required_elements.value

    @property
    def _required_elements(self) -> List:
        return self.subject.value["required"]

    def is_child_optional(self, child: Type) -> bool:
        index = Number(self._get_index(child))
        is_optional = index not in self.required_elements
        return is_optional

    def set_is_child_optional(self, child: Type, is_optional: bool) -> None:
        index = self._get_index(child)
        self.set_required(index, not is_optional)

    def _get_index(self, child: Type) -> int:
        for index, element in enumerate(self._elements.value):
            if element.structure is child.subject.structure:
                return index
        return -1

    def set_required(self, i: int, value: bool) -> None:
        self._is_element_guard(i)
        index = Number(i)
        currently_required = index in self.required_elements
        if value and not currently_required:
            self._required_elements.add_item(index)
        elif not value and currently_required:
            element = self._required_elements.value[index.value]
            self._required_elements.remove_item(element)

    def visit_list(self, subject: List):
        """Coverage calculation for List Class

        Subject may contain a type multiple times, which
        will be then matched by a single child of the List
        type multiple times.

        Args:
            subject (List): List for which coverage is calculated

        Returns:
            Coverage: of subject by self(Type)
        """
        coverage = Coverage.COVERED

        for type_node in self.elements:
            for subject_node in subject.value:
                coverage += type_node.calculate_coverage(subject_node)
        return coverage

    def __repr__(self):
        return f"ListType({self.subject.__repr__()})"
