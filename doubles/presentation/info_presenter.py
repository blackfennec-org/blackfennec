# -*- coding: utf-8 -*-

class InfoPresenterMock:
    def __init__(self):
        self.show_count = 0
        self.show_last_sender = None
        self.show_last_destination = None
        self.show_last_interpretation_service = None

    def show(self, sender, destination, interpreter):
        self.show_last_sender = sender
        self.show_last_destination = destination
        self.show_last_interpretation_service = interpreter
        self.show_count += 1
