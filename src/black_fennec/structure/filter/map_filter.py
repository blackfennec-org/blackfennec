# -*- coding: utf-8 -*-
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.filter.filter_base import FilterBase


class MapFilter(MapEncapsulationBase, FilterBase):
    """Base Class for Filter of a Map."""
    def __init__(
            self,
            visitor: 'FilterFactoryVisitor',
            subject: Map,
    ):
        MapEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        FilterBase.__init__(
            self,
            visitor,
            subject
        )

    def __repr__(self):
        return f'MapFilter({self.subject.__repr__()})'
