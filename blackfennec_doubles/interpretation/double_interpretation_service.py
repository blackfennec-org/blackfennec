# -*- coding: utf-8 -*-

class InterpretationServiceMock:
    def __init__(self, interpretations):
        self.interpretations = interpretations
        self.interpret_count = 0
        self.last_interpreted_structure = None
        self.last_specification = None

    def interpret(self, structure, specification=None):
        self.last_interpreted_structure = structure
        self.last_specification = specification
        self.interpret_count += 1
        return self.interpretations.popleft()
