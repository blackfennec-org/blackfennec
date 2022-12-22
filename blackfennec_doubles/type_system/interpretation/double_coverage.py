# -*- coding: utf-8 -*-
from blackfennec_doubles.double_dummy import Dummy


class CoverageMock:
    def __init__(self, ratio):
        self._ratio = ratio

    def is_covered(self) -> bool:
        return self._ratio != 0

    def __eq__(self, other: 'CoverageMock'):
        return self._ratio == other._ratio

    def __ne__(self, other: 'CoverageMock'):
        return self._ratio != other._ratio

    def __lt__(self, other: 'CoverageMock'):
        return self._ratio < other._ratio

    def __le__(self, other: 'CoverageMock'):
        return self._ratio <= other._ratio

    def __gt__(self, other: 'CoverageMock'):
        return self._ratio > other._ratio

    def __ge__(self, other: 'CoverageMock'):
        return self._ratio >= other._ratio

    def __hash__(self):
        return hash(self._ratio)
