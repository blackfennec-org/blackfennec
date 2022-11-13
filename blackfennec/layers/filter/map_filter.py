# -*- coding: utf-8 -*-
from blackfennec.layers.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from blackfennec.structure.map import Map
from blackfennec.layers.filter.filter_base import FilterBase


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
