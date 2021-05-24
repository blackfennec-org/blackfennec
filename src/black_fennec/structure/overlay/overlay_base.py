from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.reference import Reference


class OverlayBase(EncapsulationBase):
    """Base Class for Overlay of any Info."""
    def __init__(self, visitor, subject):
        EncapsulationBase.__init__(self, visitor, subject)

    @property
    def children(self) -> ['OverlayBase']:
        if self.subject.children:
            return [
                self._encapsulate_and_dereference(child)
                for child in self.subject.children
            ]
        else:
            return list()

    def _encapsulate_and_dereference(self, item):
        if isinstance(item, Reference):
            item = item.destination
        return item.accept(self._visitor)

    def __repr__(self):
        return f'OverlayBase({self.subject.__repr__()})'

    @staticmethod
    def _remove_encapsulation(item: Info):
        """Decapsulates a Info Class if it is encapsulated by an instance
            of OverlayBase

        Args:
            item (Info): to decapsulate.
        Returns:
            Info: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, OverlayBase):
            factory_base: OverlayBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
