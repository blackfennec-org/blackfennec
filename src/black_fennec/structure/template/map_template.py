# -*- coding: utf-8 -*-
import logging
from typing import Dict

from .template import Template
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.string import String

logger = logging.getLogger(__name__)


class MapTemplate(Template[Map], MapEncapsulationBase):
    """Base Class for Template of a Map."""

    def __init__(
        self,
        visitor,
        subject: Map,
    ):
        Template.__init__(self, visitor, subject)
        MapEncapsulationBase.__init__(self, visitor, subject)
        self._parser = visitor

    @property
    def default(self):
        return Map(
            {
                name: template.create_instance()
                for name, template in self.properties.items()
            }
        )

    def add_property(self, name, template: Template, is_required=True) -> None:
        self.subject.value["properties"].add_item(name, template.subject)
        if is_required:
            self.subject.value["required"].add_item(String(name))

    def get_name(self, structure):
        for name, prop in self.properties.items():
            if prop == structure:
                return name
        assert False, "structure is not a property"

    @property
    def required_properties(self) -> List:
        return self.subject.value["required"]

    @property
    def set_required(self, name, value):
        required: List = self.subject.value["required"]
        currently_required = name in required.list
        if value and not currently_required:
            required.add_item(name)
        elif not value and currently_required:
            required.remove_item(name)

    @property
    def properties(self) -> Dict[str, Template]:
        raw_properties: Dict[str, Structure] = self.subject.value["properties"].value

        properties = {}
        for name, structure in raw_properties.items():
            template: Template = structure.accept(self._parser)
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
                if not sub_coverage.is_covered():
                    return Coverage(1 + len(subject.value), 0)
                coverage += sub_coverage
            elif template.is_optional:
                continue
            else:
                message = f"key {name} not found in subject {subject}"
                logger.debug(message)
                return Coverage(1 + len(subject.value), 0)
        coverage += Coverage(
            len(subject.value) - len(self.properties), 0
        )  # TODO workaround
        return coverage

    def __repr__(self):
        return f"MapTemplate({self.subject.__repr__()})"
