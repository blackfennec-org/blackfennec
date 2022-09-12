# -*- coding: utf-8 -*-
import logging

from .template import Template
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.list import List

logger = logging.getLogger(__name__)


class ListTemplate(Template[List], ListEncapsulationBase):
    """Base Class for Template of a List."""

    def __init__(
        self,
        visitor: "TemplateParser",
        subject: List,
    ):
        Template.__init__(self, visitor, subject)
        ListEncapsulationBase.__init__(self, visitor, subject)

    @property
    def default(self):
        return List([template.create_instance() for template in self.elements])

    def add_element(self, template) -> None:
        self.subject.value["elements"].add_item(template.subject)

    @property
    def elements(self):
        raw_elements = self.subject.value["elements"].value

        elements = []
        for element in raw_elements:
            template = element.accept(self._visitor)
            elements.append(template)

        return elements

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
