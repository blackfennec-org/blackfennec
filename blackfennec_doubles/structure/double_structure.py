from blackfennec.structure.structure import Structure


class StructureMock:
    def __init__(self, value=None, parent=None, root=None, accept_strategy=None):
        self._value = value
        self._root = root or self
        self._parent = parent
        self._value_property_access_count = 0
        self._accept_strategy = accept_strategy or \
            (lambda self, visitor: visitor.visit_structure(self))

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def accept(self, visitor):
        return self._accept_strategy(self, visitor)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def structure(self):
        return self

    def get_root(self):
        return self._root



class StructureInstanceMock(StructureMock, Structure):
    def __init__(self, value=None, parent=None, root=None):
        StructureMock.__init__(self, value, parent, root)
        Structure.__init__(self)

    def accept(self, visitor):
        ...

    def __repr__(self) -> str:
        ...
