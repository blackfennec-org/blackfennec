import logging
from functools import lru_cache

from src.structure.info import Info
from src.structure.list import List
from src.structure.map import Map
from src.structure.template.list_template import ListTemplate
from src.structure.template.map_template import MapTemplate
from src.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class TemplateFactory:

    def create(self, subject: Info, property_storage: dict = None):
        if isinstance(subject, List):
            return ListTemplate(subject, self, property_storage)
        elif isinstance(subject, Map):
            return MapTemplate(subject, self, property_storage)
        else:
            if isinstance(subject, Info):
                subject_class = _get_template_class(subject.__class__)
                return subject_class(subject, self, property_storage)
            else:
                message = 'Can only adapt subclasses of Info, ' \
                          'but passed argument is of type({})' \
                    .format(type(subject))
                logger.error(message)
                raise TypeError(message)


@lru_cache(maxsize=32, typed=True)
def _get_template_class(subject_class: type):
    class GenericTemplate(TemplateBase, subject_class):
        def __init__(self, subject: subject_class, template_factory, property_storage):
            TemplateBase.__init__(self, subject, template_factory, property_storage)

        @property
        def subject(self) -> subject_class:
            """Property for access on encapsulated info in this TemplateAdapter."""
            return self._subject

    return GenericTemplate
