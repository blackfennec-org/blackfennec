from blackfennec.layers.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from blackfennec.structure.reference import Reference


class ReferenceEncapsulationBase(EncapsulationBase):
    """Reference implementation of the EncapsulationBase class.

    This class is used to provide a reference implementation of the
    EncapsulationBase class."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def resolve(self):
        target = self._subject.resolve()
        return self._encapsulate(target)
