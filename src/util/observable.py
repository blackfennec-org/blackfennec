# -*- coding: utf-8 -*-

class Observable():
    def __init__(self):
        self._bindings = dict()

    def _notify(self, changed_property, name):
        if name in self._bindings:
            for listener in self._bindings[name]:
                listener(self, changed_property)

    def bind(self, **kwargs):
        for key, word in kwargs.items():
            if not key in dir(self):
                raise KeyError("property {} not in self".format(key))
            if not key in self._bindings:
                self._bindings[key] = list()
            self._bindings[key].append(word)
