# -*- coding: utf-8 -*-
import os
from enum import Enum
from urllib.parse import urlparse


class UriType(Enum):
    """Enum of UriType.

    Can identify type of URI"""

    CURRENT_LOCATION = 0
    RELATIVE_PATH = 1
    ABSOLUTE_PATH = 2
    HOST_URI = 3
    UNKNOWN = 10

    @classmethod
    def from_uri(cls, uri: str):
        """Defines Type of passed uri."""
        parsed_uri = urlparse(uri)
        if parsed_uri.netloc:
            return cls.HOST_URI
        elif parsed_uri.path and str(parsed_uri.path) != '.':
            if os.path.isabs(parsed_uri.path):
                return cls.ABSOLUTE_PATH
            else:
                return cls.RELATIVE_PATH
        elif str(parsed_uri.path) == '.':
            return cls.CURRENT_LOCATION
        elif parsed_uri.fragment:
            return cls.CURRENT_LOCATION
        return cls.UNKNOWN
