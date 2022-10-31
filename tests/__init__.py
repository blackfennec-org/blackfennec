import sys
from unittest.mock import MagicMock


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = ["gi.repository"]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
