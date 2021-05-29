# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor

logger = logging.getLogger(__name__)


def create_address_template():
    """Address Template
    Defines the format of the address
    """
    template_map = Map({
        Address.FIRST_NAME_KEY: String(),
        Address.LAST_NAME_KEY: String(),
        Address.STREET_KEY: String(),
        Address.STREET_NUMBER_KEY: String(),
        Address.CITY_KEY: String()
    })

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
        self._subject: Map = map_interpretation
        if Address.FIRST_NAME_KEY not in self._subject.value:
            self.subject.add_item(Address.FIRST_NAME_KEY, String())
        if Address.LAST_NAME_KEY not in self._subject.value:
            self.subject.add_item(Address.LAST_NAME_KEY, String())
        if Address.STREET_KEY not in self._subject.value:
            self.subject.add_item(Address.STREET_KEY, String())
        if Address.STREET_NUMBER_KEY not in self._subject.value:
            self.subject.add_item(Address.STREET_NUMBER_KEY, String())
        if Address.CITY_KEY not in self._subject.value:
            self.subject.add_item(Address.CITY_KEY, String())

    @property
    def subject(self):
        return self._subject

    def _get_value(self, key):
        if key not in self.subject.value:
            return None
        return self.subject.value[key].value

    def _set_value(self, key, value):
        assert key in self.subject.value
        self.subject.value[key].value = value

    @property
    def first_name(self) -> str:
        return self._get_value(Address.FIRST_NAME_KEY)

    @first_name.setter
    def first_name(self, value: str):
        self._set_value(Address.FIRST_NAME_KEY, value)

    @property
    def last_name(self) -> str:
        return self._get_value(Address.LAST_NAME_KEY)

    @last_name.setter
    def last_name(self, value: str):
        self._set_value(Address.LAST_NAME_KEY, value)

    @property
    def street(self) -> str:
        return self._get_value(Address.STREET_KEY)

    @street.setter
    def street(self, value: str):
        self._set_value(Address.STREET_KEY, value)

    @property
    def street_number(self) -> str:
        return self._get_value(Address.STREET_NUMBER_KEY)

    @street_number.setter
    def street_number(self, value: str):
        self._set_value(Address.STREET_NUMBER_KEY, value)

    @property
    def city(self) -> str:
        return self._get_value(Address.CITY_KEY)

    @city.setter
    def city(self, value: str):
        self._set_value(Address.CITY_KEY, value)

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
