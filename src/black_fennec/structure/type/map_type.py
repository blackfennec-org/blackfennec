# -*- coding: utf-8 -*-
import logging
from typing import Dict


from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.string import String
from .type import Type

logger = logging.getLogger(__name__)


class MapType(Type[Map]):
    """Base Class for Type of a Map."""

    def __init__(self, subject: Map = None):
        subject = subject or self._type_structure()
        Type.__init__(self, subject)
    
    @staticmethod
    def _type_structure():
        return Map({"type": String("Map"), "super": Null()})

    @property
    def default(self):
        return Map(
            {name: type.create_instance() for name, type in self.properties.items()}
        )

    def is_child_optional(self, child) -> bool:
        name = String(self._get_name(child))
        is_optional = name not in self.required_properties
        return is_optional

    def set_is_child_optional(self, child, is_optional) -> None:
        name = self._get_name(child)
        self.set_required(name, not is_optional)

    def _get_name(self, structure) -> str:
        logger.debug(f"looking up name for {structure}...")
        for name, prop in self.properties.items():
            logger.debug(f"comparing {prop} to {structure}")
            if prop == structure:
                logger.debug(f"found {name}")
                return name
        raise AssertionError(f"{structure} should be a property of {self} but is not")

    def _is_property_guard(self, prop_name) -> None:
        for name, prop in self.properties.items():
            if name == prop_name:
                return
        raise AssertionError(f"{prop_name} should be a property of {self} but is not")

    @property
    def required_properties(self) -> list:
        return self._required_properties.value

    @property
    def _required_properties(self) -> List:
        if "required" not in self.subject.value:
            self.subject.add_item("required", List())
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

    @property
    def _properties(self):
        if "properties" not in self.subject.value:
            self.subject.add_item("properties", Map())
        return self.subject.value["properties"]

    def add_property(self, name, type: Type, is_required=True) -> None:
        self._properties.add_item(name, type.subject)
        if is_required:
            self._required_properties.add_item(String(name))

    @property
    def properties(self) -> Dict[str, Type]:
        raw_properties: Dict[str, Structure] = self._properties.value

        properties = {}
        for name, structure in raw_properties.items():
            from .type_parser import TypeParser
            type = TypeParser.parse(structure)
            properties[name] = type
        return properties

    def visit_map(self, subject: Map) -> Coverage:
        """Coverage calculation for Map Class

        Args:
            subject (Map): Map for which coverage is calculated

        Returns:
            Coverage: of subject by self(Type)
        """

        coverage = Coverage.COVERED

        for name, type in self.properties.items():
            if name in subject.value:
                sub_coverage = type.calculate_coverage(subject.value[name])
                if not sub_coverage.is_covered():
                    return Coverage(1 + len(subject.value), 0)
                coverage += sub_coverage
            elif type.is_optional:
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
        return f"MapType({self.subject.__repr__()})"
