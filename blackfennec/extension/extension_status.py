# -*- coding: utf-8 -*-
from enum import Enum


class ExtensionStatus(Enum):
    """Enum of Extension status.

    Represents status of extension
    """

    NOT_LOADED = 0
    LOADED = 1
    LOAD_FAILED = 2
    CREATE_FAILED = 3
    UNLOAD_FAILED = 4
