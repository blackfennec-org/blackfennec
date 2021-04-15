# -*- coding: utf-8 -*-
import logging

from src.core.types.map import Map
from src.core.types.string import String

logger = logging.getLogger(__name__)


class Address:
    def __init__(self, map_interpretation: Map = Map()):
        """Address Constructor

        Args:
            map_interpretation (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._data: Map = map_interpretation

    def _get_from_map(self, key):
        """Wrapper for map access

        Checks whether key is in map and if yes, it
        returns its value. Otherwise None is returned.

        Args:
            key (str): Key of value to check

        Returns:
            : Value at key in map
        """
        if key not in self._data:
            return None
        return self._data[key]

    @property
    def first_name(self) -> String:
        return self._get_from_map('first_name')

    @first_name.setter
    def first_name(self, value: String):
        self._data['first_name'] = value

    @property
    def last_name(self) -> String:
        return self._get_from_map('last_name')

    @last_name.setter
    def last_name(self, value: String):
        self._data['last_name'] = value

    @property
    def street(self) -> String:
        return self._get_from_map('street')

    @street.setter
    def street(self, value: String):
        self._data['street'] = value

    @property
    def street_number(self) -> String:
        return self._get_from_map('street_nr')

    @street_number.setter
    def street_number(self, value: String):
        self._data['street_nr'] = value

    @property
    def city(self) -> String:
        return self._get_from_map('city')

    @city.setter
    def city(self, value: String):
        self._data['city'] = value

    def __eq__(self, other) -> bool:
        return (
                   self.first_name,
                   self.last_name,
                   self.street,
                   self.street_number,
                   self.city
               ) == (
                   other.first_name,
                   other.last_name,
                   other.street,
                   other.street_number,
                   other.city
               )

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        """Convert to string"""
        return str(self.first_name) + ' ' + \
               str(self.last_name) + '\n' + \
               str(self.street) + ' ' + \
               str(self.street_number) + '\n' + \
               str(self.city)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Address({} {}, {} {}, {})'.format(
            self.first_name,
            self.last_name,
            self.street,
            self.street_number,
            self.city
        )
