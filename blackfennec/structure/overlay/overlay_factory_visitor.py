# -*- coding: utf-8 -*-

from blackfennec.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from blackfennec.structure.overlay.overlay_base import OverlayBase
from blackfennec.structure.reference import Reference
from blackfennec.structure.structure import Structure

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

    def visit_reference(self, subject_reference: Reference) -> Structure:
        try:
            return subject_reference.resolve().accept(self)
        except Exception:
            message = f'An unknown exception has been ignored:\n{traceback.format_exc()}'
            logger.warning(message)
            return subject_reference
