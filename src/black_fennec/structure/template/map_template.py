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


class MapTemplate(Template[Map]):
    """Base Class for Template of a Map."""

    def __init__(
        self,
        visitor: "TemplateParser",
        subject: Map,
    ):
        Template.__init__(self, visitor, subject)
        self._parser = visitor

    @property
    def default(self):
        return Map(
            {
                name: template.create_instance()
                for name, template in self.properties.items()
            }
        )


    def is_child_optional(self, child) -> bool:
        name = String(self._get_name(child))
        is_optional = name not in self.required_properties
        return is_optional

    def set_is_child_optional(self, child, is_optional) -> None:
        name = self._get_name(child)
        self.set_required(name, not is_optional)

    def _get_name(self, structure) -> str:
        for name, prop in self.properties.items():
            if prop == structure:
                return name
        raise AssertionError(f"{structure} is not a property of this class")

    def _is_property_guard(self, prop_name) -> None:
        for name, prop in self.properties.items():
            if name == prop_name:
                return
        raise AssertionError(f"{prop_name} is not a property of this class")

    @property
    def required_properties(self) -> list:
        return self._required_properties.value

    @property
    def _required_properties(self) -> List:
        return self.subject.value["required"]


    def set_required(self, name, value) -> None:
        self._is_property_guard(name)
        name = String(name)
        currently_required = name in self.required_properties
        if value and not currently_required:
            self._required_properties.add_item(name)
        elif not value and currently_required:
            for item in self.required_properties:
                if item == name:
                    self._required_properties.remove_item(item)


    def add_property(self, name, template: Template, is_required=True) -> None:
        self.subject.value["properties"].add_item(name, template.subject)
        if is_required:
            self._required_properties.add_item(String(name))

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
