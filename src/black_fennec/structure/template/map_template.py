# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class MapTemplate(MapEncapsulationBase, TemplateBase):
    """Base Class for Template of a Map."""
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Map,
    ):
        MapEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

    def visit_map(self, subject: Map):
        """Coverage calculation for Map Class

        Args:
            subject (Map): Map for which coverage is calculated

        Returns:
            (int, int): subject/template node count encountered in map
        """

        logger.debug(
            'Calculating map coverage (children=%s, types in template=%s)',
            len(subject.children),
            len(subject.children)
        )
        subject_node_count, template_node_count = super().visit_map(subject)
        if (subject_node_count, template_node_count) == TemplateBase.NOT_COVERED:
            return TemplateBase.NOT_COVERED

        subject_node_count += len(subject.children)
        for key, value in self.value.items():
            if key in subject.value:
                coverage = value.calculate_coverage(subject.value[key])
                if coverage[1] <= 0:
                    return subject_node_count, 0
                subject_node_count += coverage[0] - 1
                template_node_count += coverage[1]
            else:
                message = f'key {key} not found in subject{subject}'
                logger.debug(message)
                return subject_node_count, 0

        return subject_node_count, template_node_count

    def __repr__(self):
        return f'MapTemplate({self.subject.__repr__()})'
