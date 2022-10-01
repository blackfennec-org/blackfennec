# -*- coding: utf-8 -*-
import logging
from functools import cached_property

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.type.type import Type
from src.black_fennec.util.comparable import Comparable

logger = logging.getLogger(__name__)


class Offer(Comparable):
    """Offer that is sent to Auctioneer by StructureViewBidder.

    Only two comparison operators are implemented(eq,lt)
    the rest is included via inheritance/mixin.

    Attributes:
        _subject (Structure): Structure that is auctioned
        _specificity (Int): Describes inheritance hierarchy level
        _view_factory: View Factory for corresponding type
        _type: structure that type can handle
        _coverage (Coverage): Describes coverage of nodes of subject
    """

    def __init__(
            self,
            subject: Structure,
            type: Type
    ):
        """Offer constructor.

        Args:
            subject (Structure):
            specificity (int):
            type (Type): Type that describes type
            type_view_factory (StructureViewFactory): factory used
                to create interpretation_service
        """
        self._subject = subject
        self._type = type

    @property
    def subject(self) -> Structure:
        """subject getter

        Returns:
            Structure: subject property set by constructor
        """
        return self._subject

    @property
    def specificity(self) -> int:
        """specificity getter

        Returns:
            int: specificity property set by constructor
        """
        logger.warning("specificity hardcoded to 0")
        return 0

    @property
    def type(self) -> Type:
        """type getter

        Returns:
            Structure: Type property set by constructor
        """
        return self._type

    @cached_property
    def coverage(self) -> Coverage:
        """coverage getter

        Returns:
            float: coverage property set by constructor
        """
        return self.type.calculate_coverage(self.subject)

    def __eq__(self, other: 'Offer') -> bool:
        """Equality operator

        Arguments:
            other (Offer): Forwarding Reference because Offer
                does not exist while creating operator

        Returns:
            bool: comparison of subject, specificity and coverage with other
        """
        return (
                   self.subject,
                   self.coverage,
                   self.specificity
               ) == (
                   other.subject,
                   other.coverage,
                   other.specificity
               )

    def __lt__(self, other: 'Offer') -> bool:
        """Lower-than operator

        Arguments:
            other (Offer): to compare self with.

        Returns:
            bool: comparison of coverage and specificity with other.
                coverage is more important than specificity.
                Special case: if the coverage is equal and one of the
                two offers is an offer for a core type specificity is
                ranked in reverse order.

        Raises:
            ValueError: If the subject of the compared offers do not match
        """
        if self.subject != other.subject:
            message = 'Subject of compared offers are not equal'
            logger.error(message)
            raise ValueError(message)

        if self.coverage == other.coverage \
                and 0 in (self.specificity, other.specificity) \
                and (0, 0) != (self.specificity, other.specificity):
            return self.specificity > other.specificity

        return (
                   self.coverage,
                   self.specificity
               ) < (
                   other.coverage,
                   other.specificity
               )

    def __repr__(self):
        return f'Offer({self.type})'
