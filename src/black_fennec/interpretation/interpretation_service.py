# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.structure import Structure
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.type_system.type_registry import TypeRegistry

logger = logging.getLogger(__name__)


class InterpretationService:
    """Interpretation Service Class.

    Is produced during the selection process and is the
    Creator of Interpretations

    Attributes:
        _navigation_service (NavigationService): stores injected
            navigation service
        _auctioneer (Auctioneer): stores injected auctioneer
    """

    def __init__(self, type_registry: TypeRegistry):
        """Constructor of interpretation service

        Args:
            auctioneer (Auctioneer): selects the best offer based on the
                registered types.
        """
        self._type_registry = type_registry

    def interpret(self, structure: Structure,
                  specification: Specification = None) -> Interpretation:
        """Interpret the given structure following the a specification

        Args:
            structure (Structure): The structure to be interpreted
            specification (Specification, optional): The specification
                to be followed. Defaults to default constructed Specification.

        Returns:
            Interpretation: Represents what black fennec believes to be
                the meaning of the structure.
        """
        specification = specification or Specification()

        all_types = self._type_registry.types

        types = Auctioneer.auction(all_types, structure)
        assert len(types) == 1, 'cannot currently handle multiple types'
        interpretation = Interpretation(structure, specification, types)
        return interpretation
