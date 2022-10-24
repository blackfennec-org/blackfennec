# -*- coding: utf-8 -*-
from blackfennec.structure.structure import Structure


class NavigatorMock:
    def __init__(self, navigate_return=None):
        self.navigate_count = 0
        self.navigate_parameter_current_structure = None
        self._navigate_return = navigate_return

    def navigate(self, current_structure: Structure) -> Structure:
        self.navigate_count += 1
        self.navigate_parameter_current_structure = current_structure
        return self._navigate_return
