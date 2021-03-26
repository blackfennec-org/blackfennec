from src.core.info import Info

class Root(Info):
    def __init__(self):
        super().__init__(self)

    @property
    def parent(self):
        return super().parent

    @parent.setter
    def parent(self, new_parent):
        raise TypeError("cannot set parent on type Root")

    @property
    def root(self):
        return self
