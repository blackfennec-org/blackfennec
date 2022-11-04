from blackfennec.structure.structure import Structure
from blackfennec.util.intercepting_visitor import InterceptingVisitor


class EncapsulationBase(Structure):
    """Is the base class of the abstract visitor BaseFactoryVisitor,
        which means that any created object of the abstract visitor
        has the super class EncapsulationBase or a specialisation.

    """

    def __init__(self, visitor: 'BaseFactoryVisitor', subject: Structure):
        """Constructor for EncapsulationBase

        Args:
            visitor (BaseFactoryVisitor): visitor/abstract visitor used
                to encapsulate parent/root
            subject (Structure): subject that gets encapsulated
        """
        self._visitor = visitor
        self._subject = subject

    @property
    def subject(self):
        """Property for access on encapsulated
            structure in this EncapsulationBase."""
        return self._subject

    @property
    def parent(self):
        """Property for parent of this structure
            encapsulated in a EncapsulationBase."""
        if self.subject.parent:
            return self._encapsulate(self.subject.parent)

    @parent.setter
    def parent(self, parent: Structure):
        """Setter for parent of EncapsulationBase

        Decapsulates the passed new parent and sets
            it on the subjects parent

        Args:
            parent (Structure): new value for subjects parent
        """
        self.subject.parent = self._decapsulate(parent)

    @property
    def value(self):
        return self.subject.value

    @value.setter
    def value(self, value):
        self.subject.value = value

    def accept(self, visitor):
        interceptor = InterceptingVisitor(lambda s: self, visitor)
        return self.subject.accept(interceptor)

    def get_root(self):
        """Property for root of this structure encapsulated in an FactoryBase.

        Returns:
            EncapsulationBase: encapsulates root of subject in FactoryBase class
        """
        return self._encapsulate(self.subject.get_root())

    @property
    def structure(self):
        return self.subject.structure

    @staticmethod
    def _decapsulate(item: Structure):
        """Decapsulates a Structure Class if it is encapsulated by an instance
            of EncapsulationBase

        Args:
            item (Structure): to decapsulate.
        Returns:
            Structure: subject of passed item, if item
                is encapsulated.
        """
        decapsulated_value = item
        if isinstance(item, EncapsulationBase):
            factory_base: EncapsulationBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value

    def _encapsulate(self, subject: Structure):
        """Encapsulates a Structure Class if it is not encapsulated by an instance
            of EncapsulationBase

        Args:
            subject (Structure): to encapsulate.
            visitor (BaseFactoryVisitor): visitor/abstract visitor used
                to encapsulate parent/root
        Returns:
            Structure: subject of passed item, if item
                is encapsulated.
        """
        return subject.accept(self._visitor)

    def __repr__(self):
        return f"EncapsulationBase({self.value})"