# -*- coding: utf-8 -*-
from doubles.dummy import Dummy


class OfferFake:
    def __init__(self, value, view_factory = Dummy('ViewFactory')):
        self.value = value
        self._view_factory = view_factory

    @property
    def view_factory(self):
        return self._view_factory

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __hash__(self):
        return hash(self.value)
