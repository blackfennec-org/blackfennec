# -*- coding: utf-8 -*-

class InterpretationServiceMock:
    def __init__(self, interpretations):
        self.interpretations = interpretations
        self.interpret_count = 0
        self.last_interpreted_info = None

    def interpret(self, info):
        self.last_interpreted_info = info
        self.interpret_count += 1
        return self.interpretations.popleft()
