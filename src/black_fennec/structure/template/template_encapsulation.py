from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.structure import Structure


class TemplateEncapsulation(EncapsulationBase):
    """Base Class for Template of a any Structure.

    Contains decorating additional property optional,
        that can be set on a Template to indicate optionality
    """

    def __init__(
            self,
            visitor: 'TemplateParser',
            subject
    ):
        EncapsulationBase.__init__(self, visitor, subject)

    @property
    def parent(self):
        """Property for parent of this structure
            encapsulated in a EncapsulationBase."""
        if not self.subject.parent \
                or not self.subject.parent.parent:
            return None

        return self.subject.parent.parent.accept(self._visitor)

    @staticmethod
    def _remove_encapsulation(item: Structure):
        """Decapsulates a Structure Class if it is encapsulated by an instance
            of Template

        Args:
            item (Structure): to decapsulate.
        Returns:
            Structure: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, TemplateEncapsulation):
            factory_base: TemplateEncapsulation = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
