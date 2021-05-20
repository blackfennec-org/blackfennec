# -*- coding: utf-8 -*-
import logging
import re

from src.black_fennec.structure.info import Info
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.string_template import StringTemplate
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.util.comparable import Comparable
from src.black_fennec.interpretation.specification import Specification

logger = logging.getLogger(__name__)


class Offer(Comparable):
    """Offer that is sent to Auctioneer by InfoViewBidder.

    Only two comparison operators are implemented(eq,lt)
    the rest is included via inheritance/mixin.

    Attributes:
        _subject (Info): Info that is auctioned
        _specificity (Int): Describes inheritance hierarchy level
        _view_factory: View Factory for corresponding type
        _template: structure that type can handle
        _coverage (float): Describes coverage of nodes of subject
    """

    def __init__(
            self,
            subject: Info,
            specificity: int,
            template: TemplateBase,
            type_view_factory
    ):
        """Offer constructor.

        Args:
            subject (Info):
            specificity (int):
            template (TemplateBase): Template that describes type
            type_view_factory (InfoViewFactory): factory used
                to create interpretation_service
        """
        self._subject = subject
        self._specificity = specificity
        self._view_factory = type_view_factory
        self._template = template
        self._coverage = None

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
    def template(self) -> TemplateBase:
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

        subject_node_count, template_node_count = self.template.calculate_coverage(self.subject)

        logger.debug(
            'Received values of coverage calculation, '
            '(subject_node_count = %s, template_node_count = %s,'
            'subject_type = %s, template_type = %s)',
            subject_node_count,
            template_node_count,
            type(self.subject),
            type(self.template)
        )
        assert template_node_count <= subject_node_count, \
            'Template node count cannot be greater than subject node count'
        assert subject_node_count > 0, 'Subject node count cannot be 0'
        self._coverage = template_node_count / subject_node_count
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
                and 0 in (self.specificity, other.specificity)\
                and (0, 0) != (self.specificity, other.specificity):
            return self.specificity > other.specificity

        return (
                   self.coverage,
                   self.specificity
               ) < (
                   other.coverage,
                   other.specificity
               )

    def __hash__(self):
        return hash((self.coverage, self.specificity, self.subject))

    def __repr__(self):
        return 'Offer(%s)' % self._view_factory
