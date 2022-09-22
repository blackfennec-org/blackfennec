from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from src.black_fennec.structure.string import String
from .type_coverage_mixin import TypeCoverageMixin

T = TypeVar("T")


class Type(
    TypeCoverageMixin,
    Generic[T],
    metaclass=ABCMeta,
):
    def __init__(self, subject):
        TypeCoverageMixin.__init__(self)
        self._subject = subject

    @property
    def is_optional(self):
        if not self.parent:
            return False

        return self.parent.is_child_optional(self)

    @is_optional.setter
    def is_optional(self, value):
        assert self.parent

        self.parent.set_is_child_optional(self, value)

    @property
    def subject(self):
        return self._subject

    @property
    def parent(self):
        if not self.subject.parent \
                or not self.subject.parent.parent:
            return None
        parent_structure = self.subject.parent.parent

        from .type_parser import TypeParser
        return TypeParser.parse(parent_structure)

    @property
    @abstractmethod
    def default(self) -> T:
        ...

    def create_instance(self):
        return self.default

    def __eq__(self, o):
        return self.subject == o.subject

    def __ne__(self, other) -> bool:
        return not self == other
