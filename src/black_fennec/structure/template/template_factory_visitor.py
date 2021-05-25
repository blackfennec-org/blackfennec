from src.black_fennec.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.string_template import StringTemplate
from src.black_fennec.structure.template.template_base import TemplateBase


class TemplateFactoryVisitor(BaseFactoryVisitor):
    """Template Factory Visitor

    Class is a concrete factory which produces Template based
        info encapsulations. Only few methods are overwritten
        which require specialised functionality. For all other
        info types the abstract factory implementation suffices.
    """
    def __init__(self, metadata_storage: dict = None):
        BaseFactoryVisitor.__init__(self, TemplateBase)
        self._metadata_storage = metadata_storage if metadata_storage\
            else dict()

    @property
    def metadata_storage(self):
        """Metadata storage getter.

        Is used to keep track of the decoration attributes for
            the respecting encapsulated info. The info functions
            as key in the dictionary.

        Returns:
             dict: dictionary containing values that belong to
                a specific encapsulated info, which is used as
                key in the dictionary.
        """
        return self._metadata_storage

    def visit_string(self, subject_string: String):
        return StringTemplate(self, subject_string)

    def visit_map(self, subject_map: Map):
        return MapTemplate(self, subject_map)

    def visit_list(self, subject_list: List):
        return ListTemplate(self, subject_list)