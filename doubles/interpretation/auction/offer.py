# -*- coding: utf-8 -*-
from doubles.dummy import Dummy


class OfferFake:
    def __init__(self,
            coverage=0.5,
            view_factory=Dummy('ViewFactory'),
            satisfies=True):
        self._view_factory = view_factory
        self._satisfies = satisfies
        self._coverage = coverage

    def satisfies(self, unused_specification):
        return self._satisfies

    @property
    def coverage(self):
        return self._coverage

    @property
    def view_factory(self):
        return self._view_factory

    def __eq__(self, other):
        return self._coverage == other.coverage

    def __ne__(self, other):
        return self._coverage != other.coverage

    def __lt__(self, other):
        return self._coverage < other.coverage

    def __le__(self, other):
        return self._coverage <= other.coverage

    def __gt__(self, other):
        return self._coverage > other.coverage

    def __ge__(self, other):
        return self._coverage >= other.coverage

    def __hash__(self):
        return hash(self._coverage)
