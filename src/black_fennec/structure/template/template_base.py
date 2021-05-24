from numbers import Number

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String


class TemplateBase(EncapsulationBase):
    """Base Class for Template of a any Info.

    Contains decorating additional property optional,
        that can be set on a Template to indicate optionality
    """
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject
    ):
        EncapsulationBase.__init__(self, visitor, subject)

    @property
    def optional(self):
        if self.subject in self._visitor.metadata_storage:
            return self._visitor.metadata_storage[self.subject]
        else:
            return False

    @optional.setter
    def optional(self, value: bool):
        self._visitor.metadata_storage[self.subject] = value

    def visit_info(self, subject_info: Info) -> Coverage:
        return self._instance_equality_coverage(subject_info)

    def visit_root(self, subject_root: Root) -> Coverage:
        return self._instance_equality_coverage(subject_root)

    def visit_number(self, subject_number: Number) -> Coverage:
        return self._instance_equality_coverage(subject_number)

    def visit_boolean(self, subject_boolean: Boolean) -> Coverage:
        return self._instance_equality_coverage(subject_boolean)

    def visit_reference(self, subject_reference: Reference) -> Coverage:
        return self._instance_equality_coverage(subject_reference)

    def visit_string(self, subject_string: String) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_list(self, subject_list: List) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_map(self, subject_map: Map) -> Coverage:
        return Coverage.NOT_COVERED

    def _instance_equality_coverage(self, subject) -> Coverage:
        if isinstance(subject, self.subject.__class__):
            return Coverage.COVERED
        return Coverage.NOT_COVERED

    def calculate_coverage(self, subject):
        return subject.accept(self)

    def __repr__(self):
        return f'TemplateBase({self.subject.__repr__()})'

    @staticmethod
    def _remove_encapsulation(item: Info):
        """Decapsulates a Info Class if it is encapsulated by an instance
            of TemplateBase

        Args:
            item (Info): to decapsulate.
        Returns:
            Info: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, TemplateBase):
            factory_base: TemplateBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
