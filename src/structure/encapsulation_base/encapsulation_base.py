from src.structure.info import Info


class EncapsulationBase:
    """Is the base class of the abstract visitor BaseFactoryVisitor,
        which means that any created object of the abstract visitor
        has the super class EncapsulationBase or a specialisation.

    """
    def __init__(self, visitor: 'BaseFactoryVisitor', subject: Info):
        """Constructor for EncapsulationBase

        Args:
            visitor (BaseFactoryVisitor): visitor/abstract visitor used
                to encapsulate parent/root/children
            subject (Info): subject that gets encapsulated
        """
        self._visitor = visitor
        self._subject = subject

    @property
    def subject(self):
        """Property for access on encapsulated
            info in this EncapsulationBase."""
        return self._subject

    @property
    def parent(self):
        """Property for parent of this info
            encapsulated in a EncapsulationBase."""
        return self.subject.parent.accept(self._visitor)

    @parent.setter
    def parent(self, parent: Info):
        """Setter for parent of EncapsulationBase

        Decapsulates the passed new parent and sets
            it on the subjects parent

        Args:
            parent (Info): new value for subjects parent
        """
        decapsulated_parent = self._remove_template_class(parent)
        self.subject.parent = decapsulated_parent

    @property
    def children(self):
        if self.subject.children:
            return [
                child.accept(self._visitor)
                for child in self.subject.children
            ]
        else:
            return list()

    @property
    def root(self):
        """Property for root of this info encapsulated in an FactoryBase.

        Returns:
            EncapsulationBase: encapsulates root of subject in FactoryBase class
        """
        return self.subject.root.accept(self._visitor)

    @staticmethod
    def _remove_template_class(item: Info):
        """Decapsulates a Info Class if it is encapsulated by an instance
            of EncapsulationBase

        Args:
            item (Info): to decapsulate
        """
        decapsulated_value = item
        if isinstance(item, EncapsulationBase):
            factory_base: EncapsulationBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value

    def __repr__(self):
        return f'EncapsulationBase({self.subject.__repr__()})'
