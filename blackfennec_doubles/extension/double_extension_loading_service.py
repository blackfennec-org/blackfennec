# -*- coding: utf-8 -*-
from blackfennec_doubles.extension.double_extensions.valid_extension.double_valid_extension import ValidExtensionMock


class ExtensionLoadingServiceMock:
    def __init__(self, fail_loading=False, load_extension=ValidExtensionMock(), installed_extensions=None):
        self.sender = None
        self.name = None
        self.location = None
        self.extension = None
        self.installed_count = 0
        self.installed_extensions = installed_extensions if installed_extensions else dict()
        self.load_count = 0
        self._fail_loading = fail_loading
        self._load_extension = load_extension

    def installed(self, sender, name, location):
        self.installed_count += 1
        self.sender = sender
        self.name = name
        self.location = location
        return self.installed_extensions

    def load(self, extension):
        self.load_count += 1
        self.extension = extension
        if self._fail_loading:
            error = ValueError('Loading extension failed')
            extension.status = (ExtensionStatus.LOAD_FAILED, error)
            raise error
        else:
            return self._load_extension
