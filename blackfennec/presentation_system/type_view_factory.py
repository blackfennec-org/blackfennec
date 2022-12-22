# -*- coding: utf-8 -*-
import abc

from blackfennec.type_system.interpretation.interpretation import Interpretation
from blackfennec.type_system.interpretation.specification import Specification
from blackfennec.presentation_system.type_view import TypeView


class TypeViewFactory(metaclass=abc.ABCMeta):
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
    def create(self, interpretation: Interpretation) -> TypeView:
        """creates a view

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            View
        """
        ...
