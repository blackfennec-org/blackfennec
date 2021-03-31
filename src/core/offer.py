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

    def __init__(self, subject: Info, specificity: int, coverage: float):
        """Offer constructor.

        Args:
            subject (Info):
            specificity (int):
            coverage (float):
        """
        self._subject = subject
        self._specificity = specificity
        if coverage < 0 or coverage > 1:
            message = 'Coverage can only be in between 0 and 1'
            logger.error(message)
            raise ValueError(message)
        self._coverage = coverage

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
    def coverage(self) -> float:
        """coverage getter

        Returns:
            float: coverage property set by constructor
        """
        return self._coverage

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
