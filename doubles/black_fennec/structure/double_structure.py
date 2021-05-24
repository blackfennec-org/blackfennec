from src.black_fennec.structure.structure import Structure


class StructureMock:
    def __init__(self, value=None, parent=None, root=None):
        self._value = value
        self._root = root
        self._parent = parent
        self._value_property_access_count = 0

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def accept(self, visitor):
        return visitor.visit_structure(self)


class StructureInstanceMock(Structure, StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        Structure.__init__(self)
        StructureMock.__init__(self, value, parent, root)
