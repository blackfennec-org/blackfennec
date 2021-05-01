# -*- coding: utf-8 -*-
import os
from enum import Enum

from uri import URI


class UriType(Enum):
    CURRENT_LOCATION = 0
    RELATIVE_PATH = 1
    ABSOLUTE_PATH = 2
    HOST_URI = 3
    UNKNOWN = 10

    @classmethod
    def from_uri(cls, uri: URI):
        if uri.host:
            return cls.HOST_URI
        elif uri.path and str(uri.path) != '.':
            if os.path.isabs(uri.path):
                return cls.ABSOLUTE_PATH
            else:
                return cls.RELATIVE_PATH
        elif str(uri.path) == '.':
            return cls.CURRENT_LOCATION
        elif uri.fragment:
            return cls.CURRENT_LOCATION
        return cls.UNKNOWN
