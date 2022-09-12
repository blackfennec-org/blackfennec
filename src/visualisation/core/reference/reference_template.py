from doubles.double_dummy import Dummy
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.template.template import Template
from src.black_fennec.structure.template.template_parser import TemplateParser


class ReferenceTemplate(Template):
    """Template of reference.

    Class creates Template structure for core type
        reference."""

    def __init__(self):
        visitor = TemplateParser()
        reference_resolving_service = Dummy(
            f'ReferenceResolvingService instantiated in {__name__}')
        Template.__init__(
            self, visitor,
            Reference(reference_resolving_service))

        self._name = 'Reference'

    @property
    def default(self):
        reference_resolving_service = Dummy(
            f'ReferenceResolvingService instantiated in {__name__}')
        return Reference(reference_resolving_service)

    @property
    def name(self):
        return self._name
