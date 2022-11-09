# -*- coding: utf-8 -*-

class Observer:

    def __init__(self):
        self._calls = []

    def endpoint(self, *args, **kwargs):
        self._calls.append((args, kwargs))

    @property
    def last_call(self):
        return self._calls[-1]