# -*- coding: utf-8 -*-
from blackfennec.util.observable import Observable


class PresenterViewModelMock(Observable):
    def __init__(self, interpretations=None):
        super().__init__()
        self.show_count = 0
        self.show_last_sender = None
        self.show_last_destination = None
        self.show_last_interpreter = None
        self.set_structure_structure = None
        self.set_structure_count = 0
        self.interpretations = list() if interpretations is None \
            else interpretations

    def show(self, sender, destination):
        self.show_last_sender = sender
        self.show_last_destination = destination
        self.show_count += 1

    def set_structure(self, structure):
        self.set_structure_structure = structure
        self.set_structure_count += 1
