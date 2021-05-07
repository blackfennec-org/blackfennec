from src.structure.encapsulation_base.encapsulation_base import EncapsulationBase


class TemplateBase(EncapsulationBase):
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

    def __repr__(self):
        return f'TemplateBase({self.subject.__repr__()})'