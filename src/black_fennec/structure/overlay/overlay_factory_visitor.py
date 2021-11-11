from src.black_fennec.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.black_fennec.structure.overlay.overlay_base import OverlayBase
from src.black_fennec.structure.reference import Reference

import logging
import traceback
logger = logging.getLogger(__name__)

class OverlayFactoryVisitor(BaseFactoryVisitor):
    """Overlay Factory Visitor

    Class is a concrete factory which produces Overlay based
        structure encapsulations. Only few methods are overwritten
        which require specialised functionality. For all other
        structure types the abstract factory implementation suffices.
    """
    def __init__(self):
        BaseFactoryVisitor.__init__(self, OverlayBase)

    def visit_reference(self, subject_reference: Reference):
        try:
            return subject_reference.destination.accept(self)
        except Exception as e:
            message = f'An unknown exception has been ignored:\n{ traceback.format_exc() }'
            logger.warning(message)
            return subject_reference
