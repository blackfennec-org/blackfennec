import logging
from functools import lru_cache

from src.structure.info import Info
from src.structure.list import List
from src.structure.map import Map
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.overlay.list_overlay import ListOverlay
from src.structure.overlay.map_overlay import MapOverlay

logger = logging.getLogger(__name__)


class OverlayFactory:

    def create(self, subject: Info):
        if isinstance(subject, List):
            return ListOverlay(subject, self)
        elif isinstance(subject, Map):
            return MapOverlay(subject, self)
        else:
            if isinstance(subject, Info):
                subject_class = _get_overlay_class(subject.__class__)
                return subject_class(subject, self)
            else:
                message = 'Can only adapt subclasses of Info, ' \
                          'but passed argument is of type({})' \
                    .format(type(subject))
                logger.error(message)
                raise TypeError(message)


@lru_cache(maxsize=32, typed=True)
def _get_overlay_class(subject_class: type):
    class GenericOverlay(OverlayBase, subject_class):
        def __init__(self, subject: subject_class, overlay_factory, **kwargs):
            subject_class.__init__(self, kwargs)
            OverlayBase.__init__(self, subject, overlay_factory)

        @property
        def subject(self) -> subject_class:
            """Property for access on encapsulated info in this OverlayAdapter."""
            return self._subject

    return GenericOverlay
