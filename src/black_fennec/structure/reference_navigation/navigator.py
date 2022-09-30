# -*- coding: utf-8 -*-
import abc
import logging
from typing import Optional

from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class Navigator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def navigate(self, current: Structure) -> Structure:
        """navigates current structure and returns destination

        Returns:
            Structure: Structure navigated to
        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    @abc.abstractmethod
    def __repr__(self) -> str:
        """ Create representation for pretty printing

        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True

    def __hash__(self):
        return hash(self.__class__)
