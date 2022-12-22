# -*- coding: utf-8 -*-
from blackfennec.type_system.interpretation.coverage import Coverage
from blackfennec.structure.visitor import Visitor

from blackfennec.structure.map import Map
from blackfennec.structure.list import List
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String
from blackfennec.structure.number import Number
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.null import Null


class TypeCoverageMixin(Visitor[Coverage]):
    """Base Class for Type of a any Structure.

    Contains decorating additional property optional,
        that can be set on a Type to indicate optionality
    """
    def visit_number(self, subject: Number) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_boolean(self, subject: Boolean) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_reference(self, subject: Reference) -> Coverage:
        return self._type_equality_coverage(subject)

    def visit_string(self, unused_arg: String) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_list(self, unused_arg: List) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_map(self, unused_arg: Map) -> Coverage:
        return Coverage.NOT_COVERED

    def visit_null(self, unused_arg: Null) -> Coverage:
        return Coverage.NOT_COVERED

    def _type_equality_coverage(self, subject) -> Coverage:
        if isinstance(subject, self.subject.__class__):
            return Coverage.COVERED
        return Coverage.NOT_COVERED

    def calculate_coverage(self, subject):
        """calculate the coverage of subject by this type

        Args:
            subject (Info): The subject which should be covered

        Returns:
            Coverage: The coverage report.
        """
        return subject.accept(self)
