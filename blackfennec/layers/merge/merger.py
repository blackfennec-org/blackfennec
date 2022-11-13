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

    def visit_reference(self, overlay: Reference):
        raise TypeError("Cannot merge a reference")


class Merger(Visitor[MergedStructure]):
    def __init__(self, overlay) -> None:
        Visitor.__init__(self)
        self._overlay = overlay

    def merge(self, underlay):
        return underlay.accept(self)

    def visit_structure(self, unused_other: Structure):
        raise TypeError("cannot merge structures of different types")

    @abstractmethod
    def visit_null(self, underlay: Null):
        ...


class StringMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_string(self, underlay):
        return MergedStructure(underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedStructure(underlay, self._overlay)


class NumberMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_number(self, underlay):
        return MergedStructure(underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedStructure(underlay, self._overlay)


class BooleanMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_boolean(self, underlay):
        return MergedStructure(underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedStructure(underlay, self._overlay)


class NullMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_null(self, underlay):
        return MergedNull(underlay, self._overlay)

    def visit_map(self, subject: 'Map'):
        return MergedMap(subject, self._overlay)

    def visit_list(self, underlay):
        return MergedList(underlay, self._overlay)

    def visit_structure(self, underlay: Structure):
        return MergedStructure(underlay, self._overlay)


class ListMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_list(self, underlay):
        return MergedList(underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedList(underlay, self._overlay)


class MapMerger(Merger):
    def __init__(self, overlay):
        Merger.__init__(self, overlay)

    def visit_map(self, underlay):
        return MergedMap(underlay, self._overlay)

    def visit_null(self, underlay):
        return MergedMap(underlay, self._overlay)
