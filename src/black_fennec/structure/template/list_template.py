# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.list import List
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class ListTemplate(ListEncapsulationBase, TemplateBase):
    """Base Class for Template of a List."""

    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: List,
    ):
        ListEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

    def create_instance(self):
        return List([ template.create_instance() for template 
            in self.properties ])

    @property
    def properties(self):
        return self.value

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

        logger.debug(
            'Calculating list coverage (value=%s, types in template=%s)',
            len(subject.value),
            len(subject.value)
        )
        for template_node in self.properties:
            for subject_node in subject.value:
                coverage += template_node.calculate_coverage(subject_node)
        return coverage

    def __repr__(self):
        return f'ListTemplate({self.subject.__repr__()})'
