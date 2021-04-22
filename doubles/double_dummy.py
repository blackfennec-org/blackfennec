# -*- coding: utf-8 -*-
class Dummy:
    """Class represents a generic Dummy Double.

    This Class can be used as generic dummy."""
    def __init__(self, name="dummy"):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
