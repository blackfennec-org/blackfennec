# -*- coding: utf-8 -*-
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.type_parser import TypeParser


class MapTemplate(MapType):
    """Template of map.

    Class creates Template structure for core type
        map."""

    def __init__(self):
        MapType.__init__(self, None)

        self._name = 'Map'

    @property
    def name(self):
        return self._name
