# -*- coding: utf-8 -*-
from blackfennec.util.comparable import Comparable


class ComparableMock(Comparable):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other: 'ComparableMock'):
        return self.value == other.value

    def __lt__(self, other: 'ComparableMock'):
        return self.value < other.value
