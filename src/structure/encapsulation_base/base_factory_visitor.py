from functools import lru_cache

from src.structure.boolean import Boolean
from src.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.structure.info import Info
from src.structure.list import List
from src.structure.map import Map
from src.structure.number import Number
from src.structure.reference import Reference
from src.structure.root import Root
from src.structure.string import String


class BaseFactoryVisitor:
    """Abstract Factory and Visitor

    This class implements the base visitor behaviour
        and returns the input wrapped in an adapter/decorator
        like manner while implementing the flyweight pattern
        to save the generically generated adapter/decorator
        classes.

    Python does not support overloading by Type, thus the visit
        function are present for all existing core types.
    """

    def __init__(self, encapsulation_base_class):
        """Constructor of BaseFactoryVisitor

        Args:
            encapsulation_base_class (EncapsulationBase): contains the type of
                the visitor base, meaning that all instantiated classes
                will include this base class via multi-inheritance.
        """
        self.factory_base_class = encapsulation_base_class

    def visit_info(self, subject_info: Info):
        return self._create_generic_instance(subject_info)

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
        return ListEncapsulationBase(self, subject_list)

    def visit_map(self, subject_map: Map):
        return MapEncapsulationBase(self, subject_map)

    def _create_generic_instance(self, subject: Info):
        GenericClass = _create_generic_class(self.factory_base_class, subject.__class__)
        return GenericClass(self, subject)


@lru_cache(maxsize=32, typed=True)
def _create_generic_class(encapsulation_base_class, subject_class):

    class GenericClass(encapsulation_base_class, subject_class):
        def __init__(self, visitor, subject):
            encapsulation_base_class.__init__(self, visitor, subject)
            self.value = subject.value

    return GenericClass
