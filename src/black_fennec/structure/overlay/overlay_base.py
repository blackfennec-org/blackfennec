import logging

from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class OverlayBase(EncapsulationBase):
    """Base Class for Overlay of any Structure."""
    def __init__(self, visitor, subject):
        EncapsulationBase.__init__(self, visitor, subject)

    def __repr__(self):
        return f'OverlayBase({self.subject.__repr__()})'

    @staticmethod
    def _remove_encapsulation(item: Structure):
        """Decapsulates a Structure Class if it is encapsulated by an instance
            of OverlayBase

        Args:
            item (Structure): to decapsulate.
        Returns:
            Structure: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, OverlayBase):
            factory_base: OverlayBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
