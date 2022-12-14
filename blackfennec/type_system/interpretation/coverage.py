# -*- coding: utf-8 -*-
import logging
import math

from blackfennec.util.comparable import Comparable

logger = logging.getLogger(__name__)


class Coverage(Comparable):
    """Coverage calculated on a Type

    Only two comparison operators are implemented(eq,lt)
    the rest is included via inheritance/mixin.
    """

    NOT_COVERED = None
    COVERED = None

    def __init__(self, subject_node_count, type_node_count):
        self._subject_node_count = subject_node_count
        self._type_node_count = type_node_count

    def is_covered(self) -> bool:
        return self._type_node_count != 0

    def _calculate_ratio(self):
        assert self._subject_node_count != 0
        return self._type_node_count / self._subject_node_count

    def __iadd__(self, other: 'Coverage'):
        return Coverage(
            self._subject_node_count + other._subject_node_count,
            self._type_node_count + other._type_node_count
        )

    def __lt__(self, other: 'Coverage'):
        return self != other and\
            self._calculate_ratio() < other._calculate_ratio()

    def __repr__(self):
        return f'Coverage(' \
               f'{self._subject_node_count}, ' \
               f'{self._type_node_count})'

    def __eq__(self, other: 'Coverage'):
        return math.isclose(self._calculate_ratio(), other._calculate_ratio())

    def __hash__(self):
        return hash((self._subject_node_count, self._type_node_count))


Coverage.NOT_COVERED = Coverage(1, 0)
Coverage.COVERED = Coverage(1, 1)
