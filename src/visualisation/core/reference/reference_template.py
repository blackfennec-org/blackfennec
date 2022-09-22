from doubles.double_dummy import Dummy
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.type.reference_type import ReferenceType
from src.black_fennec.structure.type.type_parser import TypeParser


class ReferenceTemplate(ReferenceType):
    """Template of reference.

    Class creates Template structure for core type
        reference."""

    def __init__(self):
        reference_resolving_service = Dummy(
            f'ReferenceResolvingService instantiated in {__name__}')
        ReferenceType.__init__(self,
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
