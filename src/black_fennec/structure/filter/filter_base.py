from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.structure import Structure


class FilterBase(EncapsulationBase):
    """Filter Base Class

    This class contains specialised functionality
        that any Filter should be able to do.
    """

    def __init__(
            self,
            visitor: 'FilterFactoryVisitor',
            subject
    ):
        EncapsulationBase.__init__(self, visitor, subject)

    @property
    def filtered(self):
        return self._visitor.metadata_storage.get(self.subject, False)

    @filtered.setter
    def filtered(self, value: bool):
        self._visitor.metadata_storage[self.subject] = value

    def __repr__(self):
        return f'FilterBase({self.subject.__repr__()})'

    @staticmethod
    def _decapsulate(item: Structure):
        """Decapsulates a Structure Class if it is encapsulated by an instance
            of FilterBase

        Args:
            item (Structure): to decapsulate.
        Returns:
            Structure: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, FilterBase):
            factory_base: FilterBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
