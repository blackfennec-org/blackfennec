from functools import lru_cache

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String


class BaseFactoryVisitor:
    """Abstract Factory and Visitor

    This class implements the base visitor behaviour
        and returns the input wrapped in an adapter/decorator
        like manner while to save the generically generated
        adapter/decorator classes.

    Python does not support overloading by Type, thus the visit
        function are present for all existing core types.
    """

    def __init__(self, layer_base_class):
        """Constructor of BaseFactoryVisitor

        Args:
            layer_base_class (EncapsulationBase): contains the type of
                the visitor base, meaning that all instantiated classes
                will include this base class via multi-inheritance.
        """
        self.layer_base_class = layer_base_class

    def visit_structure(self, subject_structure: Structure):
        return self._create_generic_instance(subject_structure)

    def visit_root(self, subject_root: Root):
        return self._create_generic_instance(subject_root)

    def visit_string(self, subject_string: String):
        return self._create_generic_instance(subject_string)

    def visit_number(self, subject_number: Number):
        return self._create_generic_instance(subject_number)

    def visit_boolean(self, subject_boolean: Boolean):
        return self._create_generic_instance(subject_boolean)

    def visit_reference(self, subject_reference: Reference):
        return self._create_generic_instance(subject_reference)

    def visit_list(self, subject_list: List):
        ListEncapsulationClass = \
            _create_generic_collection_class(
                ListEncapsulationBase,
                self.layer_base_class
            )
        return ListEncapsulationClass(self, subject_list)

    def visit_map(self, subject_map: Map):
        MapEncapsulationClass = \
            _create_generic_collection_class(
                MapEncapsulationBase,
                self.layer_base_class
            )
        return MapEncapsulationClass(self, subject_map)

    def _create_generic_instance(self, subject: Structure):
        GenericClass = _create_generic_class(
            self.layer_base_class,
            subject.__class__
        )
        return GenericClass(self, subject)


@lru_cache(maxsize=8, typed=True)
def _create_generic_collection_class(encapsulation_base_class, layer_base_class):
    class GenericCollectionClass(encapsulation_base_class, layer_base_class):
        def __init__(self, visitor, subject):
            encapsulation_base_class.__init__(self, visitor, subject)
            layer_base_class.__init__(self, visitor, subject)

    return GenericCollectionClass


@lru_cache(maxsize=32, typed=True)
def _create_generic_class(layer_base_class, subject_class):
    """Is a static method because the lru_cache would not
        work properly with a class_method."""

    class GenericClass(layer_base_class, subject_class):
        def __init__(self, visitor, subject):
            layer_base_class.__init__(self, visitor, subject)
            subject_class.__init__(self)
            self.value = subject.value

    return GenericClass
