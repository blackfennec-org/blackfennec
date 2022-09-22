from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.type_parser import TypeParser


class ListTemplate(ListType):
    """Template of list.

    Class creates Template structure for core type
        list."""

    def __init__(self):
        ListType.__init__(self)

        self._name = 'List'

    @property
    def name(self):
        return self._name
