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


class StructureTemplateMock:
    def __init__(self, name, coverage=None):
        self._name = name
        self._coverage = coverage

    def calculate_coverage(self, subject):
        return self._coverage

    def __repr__(self):
        return self._name
