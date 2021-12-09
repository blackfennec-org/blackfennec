from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String

import logging

logger = logging.getLogger(__name__)


class DeepCopyVisitor:
    """Creates a deep copy of a structure
    """

    def visit_structure(self, subject_structure: Structure):
        message = 'The function `visit_strucutre` on `DeepCopyVisitor` ' \
                  'should never be called as this request has no meaning'
        logger.error(message)
        raise NotImplementedError(message)

    def visit_string(self, subject_string: String):
        return String(subject_string.value)

    def visit_number(self, subject_number: Number):
        return Number(subject_number.value)

    def visit_boolean(self, subject_boolean: Boolean):
        return Boolean(subject_boolean.value)

    def visit_reference(self, subject: Reference):
        return Reference(
            subject._json_reference_resolve_service,
            subject.value)

    def visit_list(self, subject: List):
        structure = List()
        for element in subject.value:
            substructure = element.accept(self)
            structure.add_item(substructure)
        return structure

    def visit_map(self, subject_map: Map):
        structure = Map()
        for key, value in subject_map.value.items():
            substructure = value.accept(self)
            structure.add_item(key, substructure)
        return structure
