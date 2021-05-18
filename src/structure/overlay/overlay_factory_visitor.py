from src.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.structure.list import List
from src.structure.map import Map
from src.structure.overlay.list_overlay import ListOverlay
from src.structure.overlay.map_overlay import MapOverlay
from src.structure.overlay.overlay_base import OverlayBase


class OverlayFactoryVisitor(BaseFactoryVisitor):
    """Overlay Factory Visitor

    Class is a concrete factory which produces Overlay based
        info encapsulations. Only few methods are overwritten
        which require specialised functionality. For all other
        info types the abstract factory implementation suffices.
    """
    def __init__(self):
        BaseFactoryVisitor.__init__(self, OverlayBase)

    def visit_map(self, subject_map: Map):
        return MapOverlay(self, subject_map)

    def visit_list(self, subject_list: List):
        return ListOverlay(self, subject_list)
