from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String


class DeepCompare:
    @staticmethod
    def compare(structure_a, structure_b):
        comparator = structure_a.accept(ComparatorFactory())
        return structure_b.accept(comparator)


class ComparatorFactory:
    """Create a comparator using the visitor pattern
    """

    def visit_structure(self, subject: Structure):
        return StructureComparator(subject)

    def visit_root(self, unused_subject: Root):
        raise NotImplementedError()

    def visit_string(self, subject: String):
        return StringComparator(subject)

    def visit_number(self, subject: Number):
        return NumberComparator(subject)

    def visit_boolean(self, subject: Boolean):
        return BooleanComparator(subject)

    def visit_reference(self, subject: Reference):
        return ReferenceComparator(subject)

    def visit_list(self, subject: List):
        return ListComparator(subject)

    def visit_map(self, subject: Map):
        return MapComparator(subject)


class ComparatorTemplate:
    """Base Comparator is a Template Pattern and always returns False.
    """

    def visit_structure(self, unused_other: Structure):
        return False

    def visit_root(self, unused_other: Root):
        return False

    def visit_string(self, unused_other: String):
        return False

    def visit_number(self, unused_other: Number):
        return False

    def visit_boolean(self, unused_other: Boolean):
        return False

    def visit_reference(self, unused_other: Reference):
        return False

    def visit_list(self, unused_other: List):
        return False

    def visit_map(self, unused_other: Map):
        return False


class StructureComparator(ComparatorTemplate):
    def __init__(self, unused_subject):
        ComparatorTemplate.__init__(self)

    def visit_structure(self, unused_other):
        return True


class StringComparator(ComparatorTemplate):
    def __init__(self, string):
        ComparatorTemplate.__init__(self)
        self._string = string

    def visit_string(self, other):
        return self._string.value == other.value


class NumberComparator(ComparatorTemplate):
    def __init__(self, number):
        ComparatorTemplate.__init__(self)
        self._number = number

    def visit_number(self, other):
        return self._number.value == other.value


class BooleanComparator(ComparatorTemplate):
    def __init__(self, boolean):
        ComparatorTemplate.__init__(self)
        self._boolean = boolean

    def visit_boolean(self, other):
        return self._boolean.value == other.value


class ReferenceComparator(ComparatorTemplate):
    def __init__(self, subject):
        ComparatorTemplate.__init__(self)
        self._subject = subject

    def visit_boolean(self, other):
        return self._subject.value == other.value


class ListComparator(ComparatorTemplate):
    """Compare structure to list via visitor pattern.
    """

    def __init__(self, subject):
        ComparatorTemplate.__init__(self)
        self._subject = subject

    def visit_list(self, other):
        if len(self._subject.value) != len(other.value):
            return False

        used = set()

        def compare_element(element):
            for other_element in other.value:
                if other_element not in used \
                        and DeepCompare.compare(element, other_element):
                    used.add(other_element)
                    return True
            return False

        for element in self._subject.value:
            if not compare_element(element):
                return False

        return True


class MapComparator(ComparatorTemplate):
    """Compare structure to map via visitor pattern.
    """

    def __init__(self, subject):
        ComparatorTemplate.__init__(self)
        self._subject = subject

    def visit_map(self, other):
        if len(self._subject.value) != len(other.value):
            return False

        for key, value in self._subject.value.items():
            if key in other.value:
                other_value = other.value[key]
                if not DeepCompare.compare(value, other_value):
                    return False
        return True
