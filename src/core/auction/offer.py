# -*- coding: utf-8 -*-
import logging

from src.core.info import Info
from src.core.types.list import List
from src.core.types.map import Map
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

    def _calculate_coverage(
            self,
            subject: Info,
            template: Info
    ):
        subject_node_count: int = 1
        template_node_count: int = 0
        if isinstance(subject, template.__class__):
            logger.debug(
                'Type of subject(%s) and template(%s) matched',
                type(subject),
                type(template)
            )
            template_node_count += 1
            if template.children:
                coverage: (int, int) = (0,0)
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
        return subject_node_count, template_node_count

    def _calculate_list_coverage(
            self,
            subject: List,
            template: List
    ):
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
            template: Map
    ):
        logger.debug(
            'Calculating map coverage (children=%s, types in template=%s)',
            len(subject.children),
            len(subject.children)
        )
        subject_node_count: int = len(subject.children)
        template_node_count: int = 0
        for key, value in template.data.items():
            if key in subject.data:
                if isinstance(subject.data[key], value.__class__):
                    subject_node_count -= 1
                coverage = self._calculate_coverage(
                    subject.data[key],
                    value
                )
                subject_node_count += coverage[0]
                template_node_count += coverage[1]
            else:
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
        return (
            self.coverage,
            self.specificity
        ) < (
            other.coverage,
            other.specificity
        )

    def __hash__(self):
        return hash((self.coverage, self.specificity, self.subject))
