# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class MapTemplate(MapEncapsulationBase, TemplateBase):
    """Base Class for Template of a Map."""

    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Map,
            is_optional: bool = False,
    ):
        MapEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        TemplateBase.__init__(
            self,
            visitor,
            subject,
            is_optional
        )
        self.factory = visitor

    def create_instance(self):
        return Map({ name: template.create_instance() for name, template
            in self.properties.items() })

    def add_property(self, name, template: TemplateBase) -> None:
        self.subject.value['properties'].add_item(name, template.subject)
        if not template.is_optional:
            self.subject.value['required'].add_item(String(name))

    @property
    def properties(self) -> dict[str, TemplateBase]:
        properties = {}
        required_properties = self.subject.value['required'].value
        raw_properties = self.subject.value['properties'].value

        for name, template_structure in raw_properties.items():
            is_optional = String(name) not in required_properties
            template = self.factory.create_template(
                template_structure, is_optional)
            properties[name] = template
        return properties

    def visit_map(self, subject: Map) -> Coverage:
        """Coverage calculation for Map Class

        Args:
            subject (Map): Map for which coverage is calculated

        Returns:
            Coverage: of subject by self(Template)
        """

        coverage = Coverage.COVERED

        for name, template in self.properties.items():
            if name in subject.value:
                sub_coverage = template.calculate_coverage(subject.value[name])
                coverage += sub_coverage
                if not sub_coverage.is_covered():
                    return Coverage(1 + len(subject.value), 0)
            elif template.is_optional:
                continue
            else:
                message = f'key {name} not found in subject {subject}'
                logger.debug(message)
                return Coverage(1 + len(subject.value), 0)
        coverage += Coverage(
            len(subject.value) - len(self.properties),
            0
        )  # TODO workaround
        return coverage

    def __repr__(self):
        return f'MapTemplate({self.subject.__repr__()})'
