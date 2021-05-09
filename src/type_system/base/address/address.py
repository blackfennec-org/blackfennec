# -*- coding: utf-8 -*-
import logging

from src.structure.map import Map
from src.structure.root import Root
from src.structure.string import String
from src.structure.template.template_factory_visitor import TemplateFactoryVisitor

logger = logging.getLogger(__name__)


def create_address_template():
    """Address Template
    Defines the format of the address
    """
    template_map = Map()
    template_map[Address.FIRST_NAME_KEY] = String()
    template_map[Address.LAST_NAME_KEY] = String()
    template_map[Address.STREET_KEY] = String()
    template_map[Address.STREET_NUMBER_KEY] = String()
    template_map[Address.CITY_KEY] = String()

    template_factory = TemplateFactoryVisitor()
    template = template_map.accept(template_factory)

    return template


class Address:
    """Address BaseType Class

    Helper class used by the address view_model representing
    the actual type 'Address'.
    Can be used by other classes as a helper to be able to
    include addresses in a overlaying datatype.
    """
    TEMPLATE = None
    FIRST_NAME_KEY = 'first_name'
    LAST_NAME_KEY = 'last_name'
    STREET_KEY = 'street'
    STREET_NUMBER_KEY = 'street_nr'
    CITY_KEY = 'city'

    def __init__(self, map_interpretation: Map = Map()):
        """Address Constructor

        Args:
            map_interpretation (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._data: Map = map_interpretation
        if Address.FIRST_NAME_KEY not in self._data:
            self._data[Address.FIRST_NAME_KEY] = String()
        if Address.LAST_NAME_KEY not in self._data:
            self._data[Address.LAST_NAME_KEY] = String()
        if Address.STREET_KEY not in self._data:
            self._data[Address.STREET_KEY] = String()
        if Address.STREET_NUMBER_KEY not in self._data:
            self._data[Address.STREET_NUMBER_KEY] = String()
        if Address.CITY_KEY not in self._data:
            self._data[Address.CITY_KEY] = String()

    def _get_from_map(self, key):
        """Wrapper for map access

        Checks whether key is in map and if yes, it
        returns its value. Otherwise None is returned.

        Args:
            key (str): Key of value to check

        Returns:
            Info: Value at key in map
        """
        if key not in self._data:
            return None
        return self._data[key].value

    @property
    def first_name(self) -> str:
        return self._get_from_map(Address.FIRST_NAME_KEY)

    @first_name.setter
    def first_name(self, value: str):
        self._data[Address.FIRST_NAME_KEY].value = value

    @property
    def last_name(self) -> str:
        return self._get_from_map(Address.LAST_NAME_KEY)

    @last_name.setter
    def last_name(self, value: str):
        self._data[Address.LAST_NAME_KEY].value = value

    @property
    def street(self) -> str:
        return self._get_from_map(Address.STREET_KEY)

    @street.setter
    def street(self, value: str):
        self._data[Address.STREET_KEY].value = value

    @property
    def street_number(self) -> str:
        return self._get_from_map(Address.STREET_NUMBER_KEY)

    @street_number.setter
    def street_number(self, value: str):
        self._data[Address.STREET_NUMBER_KEY].value = value

    @property
    def city(self) -> str:
        return self._get_from_map(Address.CITY_KEY)

    @city.setter
    def city(self, value: str):
        self._data[Address.CITY_KEY].value = value

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


Address.TEMPLATE = create_address_template()
