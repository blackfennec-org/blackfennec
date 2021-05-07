from src.structure.encapsulation_base.encapsulation_base import EncapsulationBase


class FilterBase(EncapsulationBase):
    def __init__(
            self,
            visitor: 'FilterFactoryVisitor',
            subject
    ):
        EncapsulationBase.__init__(self, visitor, subject)

    @property
    def filtered(self):
        if self.subject in self._visitor.metadata_storage:
            return self._visitor.metadata_storage[self.subject]
        else:
            return False

    @filtered.setter
    def filtered(self, value: bool):
        self._visitor.metadata_storage[self.subject] = value

    def __repr__(self):
        return f'FilterBase({self.subject.__repr__()})'
