class Info():
    def __init__(self, parent):
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def root(self):
        return self.parent.root
