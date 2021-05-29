# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
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

    def visit_map(self, subject: Map) -> Coverage:
        """Coverage calculation for Map Class

        Args:
            subject (Map): Map for which coverage is calculated

        Returns:
            Coverage: of subject by self(Template)
        """

        coverage = Coverage.COVERED

        logger.debug(
            'Calculating map coverage (value=%s, types in template=%s)',
            len(subject.value),
            len(subject.value)
        )
        for key, value in self.value.items():
            if key in subject.value:
                sub_coverage = value.calculate_coverage(subject.value[key])
                coverage += sub_coverage
                if not sub_coverage.is_covered():
                    return Coverage(1 + len(subject.value), 0)
            else:
                message = f'key {key} not found in subject{subject}'
                logger.debug(message)
                return Coverage(1 + len(subject.value), 0)
        coverage += Coverage(
            len(subject.value) - len(self.value),
            0
        )  # workaround
        return coverage

    def __repr__(self):
        return f'MapTemplate({self.subject.__repr__()})'
