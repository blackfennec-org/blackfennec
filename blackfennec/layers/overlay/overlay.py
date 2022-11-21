from blackfennec.structure.structure import Structure
from .overlay_base import OverlayBase
from . overlay_factory_visitor import OverlayFactoryVisitor
from blackfennec.util.parameterized_visitor import ParameterizedVisitor

class Overlay:
    def __init__(self):
        self._factory = OverlayFactoryVisitor(self)
        self._layer: dict[Structure, OverlayBase] = {}

    def apply(self, structure: Structure) -> OverlayBase:
        if structure in self._layer:
            return self._layer[structure]
        encap = structure.accept(self._factory)
        is_reference = ParameterizedVisitor(reference=True)
        if structure.accept(is_reference):
            return encap
        self._layer[structure] = encap
        return encap