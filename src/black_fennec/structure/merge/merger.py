from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.boolean import Boolean
from .merged import *

class MergerFactory(Visitor['Merger']):
    """Create a Merger using the visitor pattern"""

    def visit_string(self, overlay: String):
        return StringMerger(overlay)

    def visit_number(self, overlay: Number):
        return NumberMerger(overlay)

    def visit_boolean(self, overlay: Boolean):
        return BooleanMerger(overlay)

    def visit_null(self, overlay: Null):
        return NullMerger(overlay)

    def visit_list(self, overlay: List):
        return ListMerger(overlay)

    def visit_map(self, overlay: Map):
        return MapMerger(overlay)



class Merger(Visitor[MergedStructure]):
    def __init__(self, overlay) -> None:
        Visitor.__init__(self)
        self._overlay = overlay

    def merge(self, underlay):
        return underlay.accept(self)

    def visit_structure(self, unused_other: Structure):
        raise AssertionError("cannot merge structures of different types")

    def visit_null(self, underlay: Null):
        return MergedNull(underlay, self._overlay)


class StringMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_string(self, underlay):
        return MergedStructure(underlay, self._overlay)


class NumberMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_number(self, underlay):
        return MergedStructure(underlay, self._overlay)


class BooleanMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_boolean(self, underlay):
        return MergedStructure(underlay, self._overlay)


class NullMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_structure(self, underlay):
        return MergedNull(underlay, self._overlay)


class ListMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_list(self, underlay):
        return MergedList(underlay, self._overlay)


class MapMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_map(self, underlay):
        return MergedMap(underlay, self._overlay)
