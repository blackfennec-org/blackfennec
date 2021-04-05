# -*- coding: utf-8 -*-

class InfoViewFactoryMock:
    def __init__(self):
        self.creation_count = 0
        self.interpretation = None

    def create(self, interpretation):
        self.creation_count += 1
        self.interpretation = interpretation
