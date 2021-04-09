# -*- coding: utf-8 -*-
import logging

from src.base.types.address.address import Address
from src.core import Interpretation
from src.core.map import Map
from src.core.string import String

logger = logging.getLogger(__name__)


class AddressViewModel:
    """View model for core type Address."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        if not isinstance(interpretation.info, Map):
            message = 'interpretation received should be of super type Map, but is of type %s'
            logger.warning(message, type(interpretation.info))
        self._model: Address = Address(interpretation.info)

    @property
    def first_name(self):
        """Property for first name"""
        return self._model.first_name

    @first_name.setter
    def first_name(self, value: String):
        self._model.first_name = value

    @property
    def last_name(self):
        """Property for last name"""
        return self._model.last_name

    @last_name.setter
    def last_name(self, value: String):
        self._model.last_name = value

    @property
    def street(self):
        """Property for street"""
        return self._model.street

    @street.setter
    def street(self, value: String):
        self._model.street = value

    @property
    def street_number(self):
        """Property for street number"""
        return self._model.street_number

    @street_number.setter
    def street_number(self, value: String):
        self._model.street_number = value

    @property
    def city(self):
        """Property for city"""
        return self._model.city

    @city.setter
    def city(self, value: String):
        self._model.city = value
