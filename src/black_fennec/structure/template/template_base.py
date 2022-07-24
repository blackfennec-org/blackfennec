from numbers import Number

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.structure.structure import Structure


class TemplateBase(EncapsulationBase):
    """Base Class for Template of a any Structure.

    Contains decorating additional property optional,
        that can be set on a Template to indicate optionality
    """

    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject,
            is_optional: bool=False
    ):
        EncapsulationBase.__init__(self, visitor, subject)
        self.is_optional = is_optional

    @property
    def is_optional(self):
        return self._is_optional

    @is_optional.setter
    def is_optional(self, value):
        self._is_optional = value

    def visit_structure(self, subject_structure: Structure) -> Coverage:
        return self._instance_equality_coverage(subject_structure)

    def visit_number(self, subject_number: Number) -> Coverage:
        return self._instance_equality_coverage(subject_number)

    def visit_boolean(self, subject_boolean: Boolean) -> Coverage:
        return self._instance_equality_coverage(subject_boolean)

    def visit_reference(self, subject_reference: Reference) -> Coverage:
        return self._instance_equality_coverage(subject_reference)

    def visit_string(self, unused_arg: String) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_list(self, unused_arg: List) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_map(self, unused_arg: Map) -> Coverage:
        return Coverage.NOT_COVERED

    def _instance_equality_coverage(self, subject) -> Coverage:
        if isinstance(subject, self.subject.__class__):
            return Coverage.COVERED
        return Coverage.NOT_COVERED

    def calculate_coverage(self, subject):
        """calculate the coverage of subject by this template

        Args:
            subject (Info): The subject which should be covered

        Returns:
            Coverage: The coverage report.
        """
        return subject.accept(self)

    def create_instance(self):
        raise NotImplementedError()

    def __repr__(self):
        return f'TemplateBase({self.subject.__repr__()})'

    @staticmethod
    def _remove_encapsulation(item: Structure):
        """Decapsulates a Structure Class if it is encapsulated by an instance
            of TemplateBase

        Args:
            item (Structure): to decapsulate.
        Returns:
            Structure: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, TemplateBase):
            factory_base: TemplateBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
