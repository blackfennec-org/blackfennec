# -*- coding: utf-8 -*-

from blackfennec.structure.visitor import Visitor
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.structure import Structure
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.string import String
from blackfennec.structure.reference import Reference
from blackfennec.structure.null import Null

import logging

logger = logging.getLogger(__name__)


class DeepCopyVisitor(Visitor[Structure]):
    """Creates a deep copy of a structure
    """

    def visit_structure(self, subject_structure: Structure):
        message = 'The function `visit_strucutre` on `DeepCopyVisitor` ' \
                  'should never be called as this request has no meaning'
        logger.error(message)
        raise NotImplementedError(message)

    def visit_string(self, subject_string: String) -> String:
        return String(subject_string.value)

    def visit_number(self, subject_number: Number) -> Number:
        return Number(subject_number.value)

    def visit_boolean(self, subject_boolean: Boolean) -> Boolean:
        return Boolean(subject_boolean.value)

    def visit_reference(self, subject: Reference) -> Reference:
        return Reference(subject.value)

    def visit_null(self, unused_subject):
        return Null()

    def visit_list(self, subject: List) -> List:
        structure = List()
        for element in subject.value:
            substructure = element.accept(self)
            structure.add_item(substructure)
        return structure

    def visit_map(self, subject_map: Map) -> Map:
        structure = Map()
        for key, value in subject_map.value.items():
            substructure = value.accept(self)
            structure.add_item(key, substructure)
        return structure
