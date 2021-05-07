# -*- coding: utf-8 -*-
from src.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.structure.map import Map
from src.structure.template.template_base import TemplateBase


class MapTemplate(MapEncapsulationBase, TemplateBase):
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Map,
    ):
        MapEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        TemplateBase.__init__(
            self,
            visitor,
            subject
        )

    def __repr__(self):
        return f'MapTemplate({self.subject.__repr__()})'
