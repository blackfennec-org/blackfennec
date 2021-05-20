from numbers import Number

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

    NOT_COVERED = (1, 0)
    COVERED = (1, 1)

    def visit_info(self, subject_info: Info):
        return self._instance_equality_coverage(subject_info)

    def visit_root(self, subject_root: Root):
        return self._instance_equality_coverage(subject_root)

    def visit_string(self, subject_string: String):
        return self._instance_equality_coverage(subject_string)

    def visit_number(self, subject_number: Number):
        return self._instance_equality_coverage(subject_number)

    def visit_boolean(self, subject_boolean: Boolean):
        return self._instance_equality_coverage(subject_boolean)

    def visit_reference(self, subject_reference: Reference):
        return self._instance_equality_coverage(subject_reference)

    def visit_list(self, subject_list: List):
        return self._instance_equality_coverage(subject_list)

    def visit_map(self, subject_map: Map):
        return self._instance_equality_coverage(subject_map)

    def _instance_equality_coverage(self, subject):
        if isinstance(subject, self.subject.__class__):
            return self.COVERED
        return self.NOT_COVERED

    def calculate_coverage(self, subject):
        return subject.accept(self)

    def __repr__(self):
        return f'TemplateBase({self.subject.__repr__()})'
