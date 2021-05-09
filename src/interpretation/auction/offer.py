# -*- coding: utf-8 -*-
import logging
import re

from src.structure.info import Info
from src.structure.list import List
from src.structure.map import Map
from src.structure.string import String
from src.structure.template.list_template import ListTemplate
from src.structure.template.map_template import MapTemplate
from src.structure.template.template_base import TemplateBase
from src.util.comparable import Comparable
from src.interpretation.specification import Specification

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

    def _calculate_coverage(
            self,
            subject: Info,
            template: TemplateBase
    ) -> (int, int):
        """Coverage calculation for Info Class

        Args:
            subject (Info): Info for which coverage is calculated
            template (Info): Template received by type bidder
                describing how the subject should look like
                to match perfectly

        Returns:
            (int, int): subject/template node count encountered in map
        """
        subject_node_count: int = 1
        template_node_count: int = 0
        if isinstance(subject, template.subject.__class__):
            logger.debug(
                'Type of subject(%s) and template(%s) matched',
                type(subject),
                type(template.subject)
            )
            template_node_count += 1

            coverage: (int, int) = (0, 0)
            if isinstance(subject, List):
                coverage = self._calculate_list_coverage(
                    subject,
                    template
                )
            elif isinstance(subject, Map):
                coverage = self._calculate_map_coverage(
                    subject,
                    template
                )
            subject_node_count += coverage[0]
            template_node_count += coverage[1]

            if isinstance(template, String) and \
                    not self._check_pattern_match_if_has_value(
                        subject,
                        template
                    ):
                logger.info(f'Pattern mismatch of subject({subject})'
                            f' and pattern({template.value})')
                template_node_count -= 1
        else:
            logger.info(f'Type mismatch of subject({type(subject)}) and '
                        f'template({type(template.subject)})')
        return subject_node_count, template_node_count

    @staticmethod
    def _check_pattern_match_if_has_value(
            subject: String,
            template: String
    ) -> bool:
        """Check value of String for regexp

        Checks whether the value contained in the template
            if any can be matched with the strings value.

        Args:
            subject (List): String whose value has to match template
            template (List): Template that may contains value which
                if existing will be matched against the subjects value.

        Returns:
            bool: Whether value of string matches regexp if any
        """
        if template.value and template.value != '':
            if not re.match(template.value, subject.value):
                return False
        return True

    def _calculate_list_coverage(
            self,
            subject: List,
            template: ListTemplate
    ) -> (int, int):
        """Coverage calculation for List Class

        Subject may contain a type multiple times, which
        will be then matched by a single child of the List
        template multiple times.

        Args:
            subject (List): List for which coverage is calculated
            template (List): Template received by type bidder
                describing which Children of the List can be handled

        Returns:
            (int, int): subject/template node count encountered in map
        """
        logger.debug(
            'Calculating list coverage (children=%s, types in template=%s)',
            len(subject.children),
            len(subject.children)
        )
        subject_node_count: int = 0
        template_node_count: int = 0
        for template_node in template.children:
            for subject_node in subject.children:
                coverage = self._calculate_coverage(
                    subject_node,
                    template_node
                )
                subject_node_count += coverage[0]
                template_node_count += coverage[1]
        return subject_node_count, template_node_count

    def _calculate_map_coverage(
            self,
            subject: Map,
            template: MapTemplate
    ) -> (int, int):
        """Coverage calculation for Map Class

        Args:
            subject (Map): Map for which coverage is calculated
            template (Map): Template received by type bidder
                describing which Children of the Map can be handled

        Returns:
            (int, int): subject/template node count encountered in map
        """
        logger.debug(
            'Calculating map coverage (children=%s, types in template=%s)',
            len(subject.children),
            len(subject.children)
        )
        subject_node_count: int = len(subject.children)
        template_node_count: int = 0
        for key, value in template.value.items():
            if key in subject.value:
                if isinstance(subject.value[key], value.subject.__class__):
                    subject_node_count -= 1
                coverage = self._calculate_coverage(
                    subject.value[key],
                    value
                )
                if coverage[1] <= 0:
                    return subject_node_count, -1
                subject_node_count += coverage[0]
                template_node_count += coverage[1]
            else:
                logger.debug(f'key {key} not found in subject{subject}')
                return subject_node_count, -1
        return subject_node_count, template_node_count

    @property
    def coverage(self) -> float:
        """coverage getter

        Returns:
            float: coverage property set by constructor
        """
        if self._coverage:
            return self._coverage

        subject_node_count, template_node_count = self._calculate_coverage(
            self.subject,
            self.template
        )
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
                and 0 in (self.specificity, other.specificity):
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
