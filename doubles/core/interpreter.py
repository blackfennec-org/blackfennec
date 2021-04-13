# -*- coding: utf-8 -*-

class InterpreterMock:
    def __init__(self, interpretation):
        self.interpretation = interpretation
        self.interpret_count = 0
        self.last_interpreted_info = None

    def interpret(self, info):
        self.last_interpreted_info = info
        self.interpret_count += 1
        return self.interpretation
