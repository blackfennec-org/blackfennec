from collections import  UserString
from src.core.info import Info

class String(Info, UserString):
    def __init__(self, *args):
        super(Info, self).__init__(*args)

    @property
    def value(self):
        return self.data

    @value.setter
    def value(self, value):
        self.data = value
