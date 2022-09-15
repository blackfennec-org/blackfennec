# -*- coding: utf-8 -*-
import logging

from .template import Template
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.number import Number

logger = logging.getLogger(__name__)


class ListTemplate(Template[List]):
    """Base Class for Template of a List."""

    def __init__(
        self,
        visitor: "TemplateParser",
        subject: Map,
    ):
        Template.__init__(self, visitor, subject)

    @property
    def default(self):
        return List([template.create_instance() for template in self.elements])

    def add_element(self, template, is_required=True) -> None:
        self.subject.value["elements"].add_item(template.subject)
        if is_required:
            self.set_is_child_optional(template, not is_required)

    def _is_element_guard(self, index):
        if index < 0 or index >= len(self.elements):
            raise AssertionError(f"index:{index} out of range")

    @property
    def elements(self) -> list:
        raw_elements = self.subject.value["elements"].value

        elements = []
        for element in raw_elements:
            template = element.accept(self._visitor)
            elements.append(template)

        return elements

    @property
    def required_elements(self) -> list:
        return self._required_elements.value


    @property
    def _required_elements(self) -> List:
        return self.subject.value["required"]

    def is_child_optional(self, child):
        index = Number(self._get_index(child))
        is_optional = index not in self.required_elements
        return is_optional

    def set_is_child_optional(self, child, is_optional):
        index = self._get_index(child)
        self.set_required(index, not is_optional)

    def _get_index(self, child):
        for index, element in enumerate(self.elements):
            if child == element:
                return index
        return -1

    def set_required(self, index, value):
        self._is_element_guard(index)
        index = Number(index)
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
        template multiple times.

        Args:
            subject (List): List for which coverage is calculated

        Returns:
            Coverage: of subject by self(Template)
        """
        coverage = Coverage.COVERED

        for template_node in self.elements:
            for subject_node in subject.value:
                coverage += template_node.calculate_coverage(subject_node)
        return coverage

    def __repr__(self):
        return f"ListTemplate({self.subject.__repr__()})"
