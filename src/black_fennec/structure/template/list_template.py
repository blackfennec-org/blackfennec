# -*- coding: utf-8 -*-
import logging

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
                    (int, int): subject/template node count encountered in map
                """
        logger.debug(
            'Calculating list coverage (children=%s, types in template=%s)',
            len(subject.children),
            len(subject.children)
        )
        subject_node_count, template_node_count = super().visit_list(subject)
        if (subject_node_count, template_node_count) == TemplateBase.NOT_COVERED:
            return TemplateBase.NOT_COVERED

        for template_node in self.children:
            for subject_node in subject.children:
                coverage = template_node.calculate_coverage(subject_node)
                subject_node_count += coverage[0]
                template_node_count += coverage[1]
        return subject_node_count, template_node_count

    def __repr__(self):
        return f'ListTemplate({self.subject.__repr__()})'
