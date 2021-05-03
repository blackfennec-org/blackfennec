import logging
from functools import lru_cache

from src.structure.info import Info
from src.structure.list import List
from src.structure.map import Map
from src.structure.filter.list_filter import ListFilter
from src.structure.filter.map_filter import MapFilter
from src.structure.filter.filter_base import FilterBase

logger = logging.getLogger(__name__)


class FilterFactory:

    def create(self, subject: Info, property_storage: dict = None):
        if isinstance(subject, List):
            return ListFilter(subject, self, property_storage)
        elif isinstance(subject, Map):
            return MapFilter(subject, self, property_storage)
        else:
            if isinstance(subject, Info):
                subject_class = _get_filter_class(subject.__class__)
                return subject_class(subject, self, property_storage)
            else:
                message = 'Can only adapt subclasses of Info, ' \
                          'but passed argument is of type({})' \
                    .format(type(subject))
                logger.error(message)
                raise TypeError(message)


@lru_cache(maxsize=32, typed=True)
def _get_filter_class(subject_class: type):
    class GenericFilter(FilterBase, subject_class):
        def __init__(
                self,
                subject: subject_class,
                filter_factory,
                property_storage
        ):
            FilterBase.__init__(
                self,
                subject,
                filter_factory,
                property_storage
            )

        @property
        def subject(self) -> subject_class:
            """Property for access on encapsulated info
                in this FilterAdapter."""
            return self._subject

    return GenericFilter
