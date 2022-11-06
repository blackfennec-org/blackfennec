# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.structure import Structure
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.specification import Specification
from blackfennec.interpretation.auction.offer import Offer
from blackfennec.type_system.type_registry import TypeRegistry
from blackfennec.type_system.type import Type

logger = logging.getLogger(__name__)


class InterpretationService:
    """Interpretation Service Class.

    Is produced during the selection process and is the
    Creator of Interpretations
    """

    def __init__(self, type_registry: TypeRegistry):
        self._type_registry = type_registry

    def interpret(self, 
            structure: Structure,
            specification: Specification) -> Interpretation:
        """Interpret the given structure following the a specification

        Args:
            structure (Structure): The structure to be interpreted
            specification (Specification, optional): The specification
                to be followed. Defaults to default constructed Specification.

        Returns:
            Interpretation: Represents what black fennec believes to be
                the meaning of the structure.
        """
        all_types = self._type_registry.types

        offers = self._create_offers(structure, all_types)
        acceptable_offers = self._filter_offers(offers)
        sorted_offers = self._sort_offers(acceptable_offers)
        interpreted_types = self._extract_types(sorted_offers)
        return Interpretation(structure, specification, interpreted_types)
    
    @classmethod
    def _create_offers(cls, structure: Structure, types: list[Type]) -> list[Offer]:
        """Create offers for the structure for each type in types

        Args:
            structure (Structure): The structure to be interpreted
            types (list): The types to be considered
        """
        return (Offer(structure, type) for type in types)

    @classmethod
    def _filter_offers(cls, offers: list[Offer]) -> list[Offer]:
        """Filter out offers that are not acceptable

        Args:
            offers (list[Offer]): The offers to be filtered

        Returns:
            list[Offer]: The filtered offers
        """
        return (offer for offer in offers if offer.coverage.is_covered())

    @classmethod
    def _sort_offers(cls, offers: list[Offer]) -> list[Offer]:
        """Sort the offers

        Args:
            offers (list[Offer]): The offers to be sorted

        Returns:
            list[Offer]: The sorted offers
        """
        return reversed(sorted(offers))

    @classmethod
    def _extract_types(cls, offers: list[Offer]) -> list[Type]:
        """Extract the types from the offers

        Args:
            offers (list[Offer]): The offers to be extracted from

        Returns:
            list[Type]: The extracted types
        """
        return (offer.type for offer in offers)
