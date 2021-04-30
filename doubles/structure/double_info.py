from src.structure.info import Info


class InfoMock:
    def __init__(self, value=None, children=None, parent=None, root=None):
        self._root = root
        self._parent = parent
        self._value_property_access_count = 0
        self._value_history = [value]
        self._children_property_access_count = 0
        self._children = children

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value_history[-1]

    @value.setter
    def value(self, value):
        self._value_history.append(value)

    @property
    def children(self):
        self._children_property_access_count += 1
        return self._children

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

class InfoInstanceMock(Info, InfoMock):
    def __init__(self, value=None, children=None, parent=None, root=None):
        Info.__init__(self)
        InfoMock.__init__(self, value, children, parent, root)
