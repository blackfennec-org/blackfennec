# -*- coding: utf-8 -*-
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.visitor import Visitor

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.null import Null


class TemplateCoverageMixin(Visitor[Coverage]):
    """Base Class for Template of a any Structure.

    Contains decorating additional property optional,
        that can be set on a Template to indicate optionality
    """
    def visit_number(self, subject: Number) -> Coverage:
        return self._type_equality_coverage(subject)

    def visit_boolean(self, subject: Boolean) -> Coverage:
        return self._type_equality_coverage(subject)

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
        """calculate the coverage of subject by this template

        Args:
            subject (Info): The subject which should be covered

        Returns:
            Coverage: The coverage report.
        """
        return subject.accept(self)
