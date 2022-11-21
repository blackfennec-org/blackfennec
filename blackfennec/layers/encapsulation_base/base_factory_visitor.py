# -*- coding: utf-8 -*-
from functools import lru_cache

from typing import TypeVar

from blackfennec.layers.encapsulation_base.reference_encapsulation_base import \
    ReferenceEncapsulationBase
from blackfennec.structure.visitor import Visitor
from blackfennec.structure.boolean import Boolean
from blackfennec.layers.encapsulation_base.list_encapsulation_base import \
    ListEncapsulationBase
from blackfennec.layers.encapsulation_base.map_encapsulation_base import \
    MapEncapsulationBase
from blackfennec.structure.structure import Structure
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.string import String
from blackfennec.structure.reference import Reference
from blackfennec.structure.null import Null

T = TypeVar('T')


class BaseFactoryVisitor(Visitor[T]):
    """Abstract Factory and Visitor

    This class implements the base visitor behaviour
        and returns the input wrapped in an adapter/decorator
        like manner while caching the generated generic
        adapter/decorator classes.

    Python does not support overloading by Type, thus the visit
        function are present for all existing core types.
    """

    def __init__(self, layer, layer_base_class):
        """Constructor of BaseFactoryVisitor

        Args:
            layer_base_class (EncapsulationBase): contains the type of
                the visitor base, meaning that all instantiated classes
                will include this base class via multi-inheritance.
        """
        self._layer = layer
        self.layer_base_class = layer_base_class

    def visit_structure(self, subject: Structure) -> T:
        return self._create_generic_instance(subject)

    def visit_string(self, subject: String) -> T:
        return self._create_generic_instance(subject)

    def visit_number(self, subject: Number) -> T:
        return self._create_generic_instance(subject)

    def visit_boolean(self, subject: Boolean) -> T:
        return self._create_generic_instance(subject)

    def visit_reference(self, subject: Reference) -> T:
        ReferenceEncapsulationClass = \
            _create_generic_encapsulation_class(
                ReferenceEncapsulationBase,
                self.layer_base_class
            )
        return ReferenceEncapsulationClass(self._layer, subject)

    def visit_null(self, subject: Null) -> T:
        return self._create_generic_instance(subject)

    def visit_list(self, subject: List) -> T:
        ListEncapsulationClass = \
            _create_generic_encapsulation_class(
                ListEncapsulationBase,
                self.layer_base_class
            )
        return ListEncapsulationClass(self._layer, subject)

    def visit_map(self, subject: Map) -> T:
        MapEncapsulationClass = \
            _create_generic_encapsulation_class(
                MapEncapsulationBase,
                self.layer_base_class
            )
        return MapEncapsulationClass(self._layer, subject)

    def _create_generic_instance(self, subject: Structure):
        GenericClass = _create_generic_class(self.layer_base_class)
        return GenericClass(self._layer, subject)


@lru_cache(maxsize=8, typed=True)
def _create_generic_encapsulation_class(
        encapsulation_base_class,
        layer_base_class
):
    class GenericCollectionClass(encapsulation_base_class, layer_base_class):
        def __init__(self, layer, subject):
            encapsulation_base_class.__init__(self, layer, subject)
            layer_base_class.__init__(self, layer, subject)

    return GenericCollectionClass


@lru_cache(maxsize=32, typed=True)
def _create_generic_class(layer_base_class):
    """Is a static method because the lru_cache would not
        work properly with a class_method."""

    class GenericClass(layer_base_class):
        def __init__(self, layer, subject):
            layer_base_class.__init__(self, layer, subject)

    return GenericClass
