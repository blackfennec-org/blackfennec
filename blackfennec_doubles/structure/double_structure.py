from blackfennec.structure.structure import Structure
from blackfennec.util.observable import Observable
from blackfennec_doubles.util.double_change_notification import ChangeNotificationMock


class StructureMock(Observable):
    def __init__(
            self,
            value=None,
            parent=None,
            root=None,
            accept_strategy=None
    ):
        super().__init__()
        self._value = value
        self._root = root or self
        self._parent = parent
        self._value_property_access_count = 0
        self._accept_strategy = accept_strategy or (
            lambda self, visitor: visitor.visit_structure(self))

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

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value


class NotifyingStructureMock(StructureMock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def value(self):
        return super().value
    
    @value.setter
    def value(self, new_value):
        notification = ChangeNotificationMock(self.value, new_value)
        StructureMock.value.fset(self, new_value)
        self._notify('changed', notification)


class StructureInstanceMock(StructureMock, Structure):
    def __init__(self, value=None, parent=None, root=None):
        StructureMock.__init__(self, value, parent, root)
        Structure.__init__(self)

    def accept(self, visitor):
        ...

    def __repr__(self) -> str:
        ...
