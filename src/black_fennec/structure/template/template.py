from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from src.black_fennec.structure.string import String

from .template_coverage_mixin import TemplateCoverageMixin
from .template_encapsulation import TemplateEncapsulation

T = TypeVar("T")


class Template(
    TemplateEncapsulation,
    TemplateCoverageMixin,
    Generic[T],
    metaclass=ABCMeta,
):
    def __init__(self, visitor, subject):
        TemplateEncapsulation.__init__(self, visitor, subject)
        TemplateCoverageMixin.__init__(self)

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
    @abstractmethod
    def default(self) -> T:
        ...

    def create_instance(self):
        return self.default

    def __eq__(self, o):
        return self.subject == o.subject

    def __ne__(self, other) -> bool:
        return not self == other
