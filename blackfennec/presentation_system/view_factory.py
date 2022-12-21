# -*- coding: utf-8 -*-
import abc

from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.specification import Specification
from blackfennec.presentation_system.view import View


class ViewFactory(metaclass=abc.ABCMeta):
    """Base class for all view factories.

    A view factory is a class that creates views for a specific type.
    """

    @abc.abstractmethod
    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        ...

    @abc.abstractmethod
    def create(self, interpretation: Interpretation) -> View:
        """creates a view

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            View
        """
        ...
