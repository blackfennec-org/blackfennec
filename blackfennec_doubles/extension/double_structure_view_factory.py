# -*- coding: utf-8 -*-

class StructureViewFactoryMock:
    def __init__(self, view=None):
        self.creation_count = 0
        self.interpretation = None
        self._view = view

    def create(self, interpretation):
        self.creation_count += 1
        self.interpretation = interpretation
        return self._view
