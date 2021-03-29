# -*- coding: utf-8 -*-
import logging
from src.util.comparable import Comparable

logger = logging.getLogger(__name__)


class Offer(Comparable):
    """Offer that is sent to Bidder by InfoViewBidder.

    Only two comparison operators are implemented(eq,lt)
    the rest is included via inheritance/mixin.

    Attributes:
        _info (Info): Info that is auctioned
        _covered ([Info]): Describes covered nodes of Info that is auctioned
        _specificity (Int): Describes inheritance hierarchy level
    """

    def __init__(self, info, specificity: int, covered):
        """Offer constructor.

        Args:
            info (Info):
            covered ([Info]):
            specificity (int):
        """
        self._info = info
        self._covered = covered
        self._specificity = specificity

    @property
    def specificity(self):
        """specificity getter

        Returns:
            int: specificity property set by constructor
        """
        return self._specificity

    @property
    def covered(self):
        """covered getter

        List all nodes covered by offer

        Returns:
            [Info]: covered nodes of info
        """
        return self._coverage

    @property
    def coverage(self):
        """coverage getter

        Calculation of coverage

        Returns:
            float: coverage property set by constructor
        """
        if self._info == self._covered:
            return 1.0

    def __eq__(self, other: 'Offer'):
        """Equality operator

        Arguments:
            other (Offer): Forwarding Reference because Offer
                does not exist while creating operator

        Returns:
            bool: comparison of specificity and coverage with other
        """
        return (self.specificity == other.specificity) and \
               (self.coverage == other.coverage)

    def __lt__(self, other: 'Offer'):
        """Lower-than operator

        Arguments:
            other (Offer): Forwarding Reference because Offer
                does not exist while creating operator

        Returns:
            bool: comparison of specificity and coverage with other.
                specificity is more important than coverage
        """
        if self.specificity == other.specificity:
            return self.coverage < other.coverage
        else:
            return self.specificity < other.specificity
