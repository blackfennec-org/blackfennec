from abc import abstractmethod
from blackfennec.structure.visitor import Visitor
from blackfennec.structure.structure import Structure
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.reference import Reference
from blackfennec.structure.null import Null
from blackfennec.structure.string import String
from blackfennec.structure.number import Number
from blackfennec.structure.boolean import Boolean
from .merged_structure import MergedStructure
from .merged_null import MergedNull
from .merged_list import MergedList
from .merged_map import MergedMap


class MergerFactory(Visitor["Merger"]):
    """Create a Merger using the visitor pattern"""

    def __init__(self, layer) -> None:
        super().__init__()
        self._layer = layer

    def create(self, overlay: Structure):
        return overlay.accept(self)

    def visit_string(self, overlay: String):
        return StringMerger(self._layer, overlay)

    def visit_number(self, overlay: Number):
        return NumberMerger(self._layer, overlay)

    def visit_boolean(self, overlay: Boolean):
        return BooleanMerger(self._layer, overlay)

    def visit_null(self, overlay: Null):
        return NullMerger(self._layer, overlay)

    def visit_list(self, overlay: List):
        return ListMerger(self._layer, overlay)

    def visit_map(self, overlay: Map):
        return MapMerger(self._layer, overlay)

    def visit_reference(self, overlay: Reference):
        raise TypeError("Cannot merge a reference")


class Merger(Visitor[MergedStructure]):
    def __init__(self, layer, overlay) -> None:
        Visitor.__init__(self)
        self._overlay = overlay
        self._layer = layer

    def merge(self, underlay):
        return underlay.accept(self)

    def visit_structure(self, unused_other: Structure):
        raise TypeError("cannot merge structures of different types")

    @abstractmethod
    def visit_null(self, underlay: Null):
        ...


class StringMerger(Merger):
    def __init__(self, layer, overlay):
        super().__init__(layer, overlay)

    def visit_string(self, underlay):
        return MergedStructure(self._layer, underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedStructure(self._layer, underlay, self._overlay)


class NumberMerger(Merger):
    def __init__(self, layer, overlay):
        super().__init__(layer, overlay)

    def visit_number(self, underlay):
        return MergedStructure(self._layer, underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedStructure(self._layer, underlay, self._overlay)


class BooleanMerger(Merger):
    def __init__(self, layer, overlay):
        super().__init__(layer, overlay)

    def visit_boolean(self, underlay):
        return MergedStructure(self._layer, underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedStructure(self._layer, underlay, self._overlay)


class NullMerger(Merger):
    def __init__(self, layer, overlay):
        super().__init__(layer, overlay)

    def visit_null(self, underlay):
        return MergedNull(self._layer, underlay, self._overlay)

    def visit_map(self, underlay: 'Map'):
        return MergedMap(self._layer, underlay, self._overlay)

    def visit_list(self, underlay):
        return MergedList(self._layer, underlay, self._overlay)

    def visit_structure(self, underlay: Structure):
        return MergedStructure(self._layer, underlay, self._overlay)


class ListMerger(Merger):
    def __init__(self, layer, overlay):
        super().__init__(layer, overlay)

    def visit_list(self, underlay):
        return MergedList(self._layer, underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedList(self._layer, underlay, self._overlay)


class MapMerger(Merger):
    def __init__(self, layer, overlay):
        super().__init__(layer, overlay)

    def visit_map(self, underlay):
        return MergedMap(self._layer, underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedMap(self._layer, underlay, self._overlay)
