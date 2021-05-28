from numbers import Number

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String
from src.black_fennec.structure.visitors.deep_copy_visitor import \
    DeepCopyVisitor


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

    def visit_string(self, unused_subject: String) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_list(self, unused_subject: List) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_map(self, unused_subject: Map) -> Coverage:
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

    def create_structure(self):
        return self.subject.accept(DeepCopyVisitor())

    def __repr__(self):
        return f'TemplateBase({self.subject.__repr__()})'
