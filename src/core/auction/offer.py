# -*- coding: utf-8 -*-
import logging

from src.core.info import Info
from src.util.comparable import Comparable

logger = logging.getLogger(__name__)


class Offer(Comparable):
    """Offer that is sent to Auctioneer by InfoViewBidder.

    Only two comparison operators are implemented(eq,lt)
    the rest is included via inheritance/mixin.

    Attributes:
        _subject (Info): Info that is auctioned
        _specificity (Int): Describes inheritance hierarchy level
        _coverage (float): Describes coverage of nodes of subject
    """

    def __init__(
            self,
            subject: Info,
            specificity: int,
            template: Info,
            type_view_factory
    ):
        """Offer constructor.

        Args:
            subject (Info):
            specificity (int):
            template (Info): Template that describes type
            type_view_factory (InfoViewFactory): factory used
                to create interpreter
        """
        self._subject = subject
        self._specificity = specificity
        self._view_factory = type_view_factory
        self._template = template
        self._coverage = None

    @property
    def subject(self) -> Info:
        """subject getter

        Returns:
            Info: subject property set by constructor
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
    def template(self) -> Info:
        """template getter

        Returns:
            Info: Template property set by constructor
        """
        return self._template

    @property
    def coverage(self) -> float:
        """coverage getter

        Returns:
            float: coverage property set by constructor
        """
        if self._coverage:
            return self._coverage
        self._coverage = float(
            isinstance(self._subject, self._template.__class__)
        )
        return self._coverage

    @property
    def view_factory(self):
        """view_factory getter

        Returns:
             InfoViewFactory: info_view factory property set by constructor
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
            other (Offer): Forwarding Reference because Offer
                does not exist while creating operator

        Returns:
            bool: comparison of specificity and coverage with other.
                specificity is more important than coverage
        """
        if self.subject != other.subject:
            message = 'Subject of compared offers are not equal'
            logger.error(message)
            raise ValueError(message)
        return self.coverage < other.coverage

    def __hash__(self):
        return hash((self.coverage, self.specificity, self.subject))
