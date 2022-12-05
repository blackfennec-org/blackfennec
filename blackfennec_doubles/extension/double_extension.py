# -*- coding: utf-8 -*-
from blackfennec.extension.extension import Extension
from blackfennec_doubles.structure.double_map import MapMock


class ExtensionMock:
    def __init__(self, name, dependencies=None, expected_state=Extension.State.ACTIVE):
        self.name = name
        self.dependencies = dependencies or set()
        self.expected_state = expected_state
        self.state = None
       
    def activate(self):
        if self.expected_state == Extension.State.FAILED:
            raise Exception('Extension failed to activate')

    def assert_state(self):
        assert self.state == self.expected_state, f'Extension {self.name} expected state {self.expected_state} but was {self.state}'
