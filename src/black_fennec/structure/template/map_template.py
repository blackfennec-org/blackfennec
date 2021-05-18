# -*- coding: utf-8 -*-
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.template_base import TemplateBase


class MapTemplate(MapEncapsulationBase, TemplateBase):
    """Base Class for Template of a Map."""
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
