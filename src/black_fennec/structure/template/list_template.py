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
        coverage = super().visit_list(subject)
        if not coverage.is_covered():
            return Coverage.NOT_COVERED

        logger.debug(
            'Calculating list coverage (children=%s, types in template=%s)',
            len(subject.children),
            len(subject.children)
        )
        for template_node in self.children:
            for subject_node in subject.children:
                coverage += template_node.calculate_coverage(subject_node)
        return coverage

    def __repr__(self):
        return f'ListTemplate({self.subject.__repr__()})'
