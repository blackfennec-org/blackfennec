# -*- coding: utf-8 -*-

class InfoViewFactoryMock:
    def __init__(self, view=None):
        self.creation_count = 0
        self.interpretation = None
        self.specification = None
        self._view = view

    def create(self, interpretation, specification):
        self.creation_count += 1
        self.interpretation = interpretation
        self.specification = specification
        return self._view
