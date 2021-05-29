import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.address.address import Address
from src.visualisation.base.address.address_view_model import AddressViewModel


class AddressViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressViewModel(InterpretationMock(MapMock()))

    def test_can_get_first_name(self):
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.first_name, '')

    def test_first_name_getter(self):
        data = dict()
        data[Address.FIRST_NAME_KEY] = StringMock('first_name')

        data_map = MapMock(data)
        view_model = AddressViewModel(InterpretationMock(data_map))
        self.assertEqual(
            view_model.first_name,
            data[Address.FIRST_NAME_KEY].value
        )

    def test_first_name_setter(self):
        first_name = Address.FIRST_NAME_KEY
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        view_model.first_name = first_name
        self.assertEqual(view_model.first_name, first_name)

    def test_can_get_last_name(self):
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.last_name, '')

    def test_last_name_getter(self):
        data = dict()
        data[Address.LAST_NAME_KEY] = StringMock('last_name')

        data_map = MapMock(data)
        view_model = AddressViewModel(InterpretationMock(data_map))
        self.assertEqual(
            view_model.last_name,
            data[Address.LAST_NAME_KEY].value
        )

    def test_last_name_setter(self):
        last_name = Address.LAST_NAME_KEY
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        view_model.last_name = last_name
        self.assertEqual(view_model.last_name, last_name)

    def test_can_get_street(self):
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.street, '')

    def test_street_getter(self):
        data = dict()
        data[Address.STREET_KEY] = StringMock('street')

        data_map = MapMock(data)
        view_model = AddressViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.street, data[Address.STREET_KEY].value)

    def test_street_setter(self):
        street = Address.STREET_KEY
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        view_model.street = street
        self.assertEqual(view_model.street, street)

    def test_can_get_street_number(self):
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.street_number, '')

    def test_street_number_getter(self):
        data = dict()
        data[Address.STREET_NUMBER_KEY] = StringMock('street_nr')

        data_map = MapMock(data)
        view_model = AddressViewModel(InterpretationMock(data_map))
        self.assertEqual(
            view_model.street_number,
            data[Address.STREET_NUMBER_KEY].value
        )

    def test_street_number_setter(self):
        street_number = Address.STREET_NUMBER_KEY
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        view_model.street_number = street_number
        self.assertEqual(view_model.street_number, street_number)

    def test_can_get_city(self):
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.city, '')

    def test_city_getter(self):
        data = dict()
        data[Address.CITY_KEY] = StringMock('city')

        data_map = MapMock(data)
        view_model = AddressViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.city, data[Address.CITY_KEY].value)

    def test_city_setter(self):
        city = Address.CITY_KEY
        view_model = AddressViewModel(InterpretationMock(MapMock()))
        view_model.city = city
        self.assertEqual(view_model.city, city)
