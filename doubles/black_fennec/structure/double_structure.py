from src.black_fennec.structure.structure import Structure


class StructureMock:
    def __init__(self, value=None, parent=None, root=None):
        self._value = value
        self._root = root or self
        self._parent = parent or self
        self._value_property_access_count = 0

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def accept(self, visitor):
        return visitor.visit_structure(self)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def get_root(self):
        return self._root



class StructureInstanceMock(Structure, StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        Structure.__init__(self, value)
        StructureMock.__init__(self, value, parent, root)

    def accept(self, visitor):
        ...

    def __repr__(self) -> str:
        ...
