# -*- coding: utf-8 -*-
class CreateFailingExtensionMock:
    def __init__(self):
        self.create_extension_count = 0
        self.destroy_extension_count = 0
        self.extension_api = None

    def create_extension(self, extension_api):
        self.create_extension_count += 1
        self.extension_api = extension_api
        raise ValueError('Creation failed')

    def destroy_extension(self, extension_api):
        self.destroy_extension_count += 1
        self.extension_api = extension_api
