# -*- coding: utf-8 -*-
import logging
from functools import cached_property

from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.template.template_base import TemplateBase
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
        _template: structure that type can handle
        _coverage (Coverage): Describes coverage of nodes of subject
    """

    def __init__(
            self,
            subject: Structure,
            specificity: int,
            template: TemplateBase,
            type_view_factory
    ):
        """Offer constructor.

        Args:
            subject (Structure):
            specificity (int):
            template (TemplateBase): Template that describes type
            type_view_factory (StructureViewFactory): factory used
                to create interpretation_service
        """
        self._subject = subject
        self._specificity = specificity
        self._view_factory = type_view_factory
        self._template = template

    def satisfies(self, specification: Specification):
        """Evaluates this offers capability to satisfy a given specification.

        Args:
            specification (Specification): The specification which must be
                satisfyable for this function to return true.

        Returns:
            bool: True iff specification can be satisfied. Otherwise False.
        """
        return self._view_factory.satisfies(specification)

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
        return self._specificity

    @property
    def template(self) -> TemplateBase:
        """template getter

        Returns:
            Structure: Template property set by constructor
        """
        return self._template

    @cached_property
    def coverage(self) -> Coverage:
        """coverage getter

        Returns:
            float: coverage property set by constructor
        """
        return self.template.calculate_coverage(self.subject)

    @property
    def view_factory(self):
        """view_factory getter

        Returns:
             StructureViewFactory: structure_view factory
                property set by constructor
        """
        return self._view_factory

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
        return f'Offer({self._view_factory})'
