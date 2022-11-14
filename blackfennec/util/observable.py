# -*- coding: utf-8 -*-

class Observable:
    """
    Observable Class

    Base for Observable used in Observer Pattern.
    """

    def __init__(self):
        self._bindings = {}

    def _notify(self, key, notification, sender=None):
        sender = sender or self
        if key in self._bindings:
            for listener in self._bindings[key]:
                listener(sender, notification)

    def bind(self, **kwargs):
        for key, word in kwargs.items():
            if key not in self._bindings:
                self._bindings[key] = []
            self._bindings[key].append(word)
