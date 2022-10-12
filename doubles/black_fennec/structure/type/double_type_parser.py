from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.encapsulation_base.list_encapsulation_base import ListEncapsulationBase
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.type.string_type import StringType
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.type import Type


class TypeParserMock(FactoryBaseVisitorMock):
    def __init__(self):
        FactoryBaseVisitorMock.__init__(self)

    def visit_structure(self, subject_structure):
        subject_structure = super().visit_structure(subject_structure)
        Encapsulation = _create_generic_class(Type)
        return Encapsulation(self, subject_structure)

    def visit_root(self, subject_root):
        subject_root = super().visit_root(subject_root)
        Encapsulation = _create_generic_class(Type)
        return Encapsulation(self, subject_root)

    def visit_number(self, subject_number):
        subject_number = super().visit_number(subject_number)
        Encapsulation = _create_generic_class(Type)
        return Encapsulation(self, subject_number)

    def visit_boolean(self, subject_boolean):
        subject_boolean = super().visit_boolean(subject_boolean)
        Encapsulation = _create_generic_class(Type)
        return Encapsulation(self, subject_boolean)

    def visit_reference(self, subject_reference):
        subject_reference = super().visit_reference(subject_reference)
        Encapsulation = _create_generic_class(Type)
        return Encapsulation(self, subject_reference)

    def visit_string(self, subject_string):
        subject_string = super().visit_string(subject_string)
        return StringType(self, subject_string)

    def visit_list(self, subject_list):
        subject_list = super().visit_list(subject_list)
        return ListType(self, subject_list)

    def visit_map(self, subject_map):
        subject_map = super().visit_map(subject_map)
        return MapType(self, subject_map)
        
    def visit_null(self, subject):
        subject = super().visit_null(subject)
        return NullType(self, subject)


    @property
    def metadata_storage(self):
        return self._metadata_storage