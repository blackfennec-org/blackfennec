import unittest
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.address.address import Address


class AddressTestSuite(unittest.TestCase):
    def test_can_construct(self):
        address = Address()
        self.assertEqual(address.first_name, '')
        self.assertEqual(address.last_name, '')
        self.assertEqual(address.street, '')
        self.assertEqual(address.street_number, '')
        self.assertEqual(address.city, '')

    def test_can_construct_with_map(self):
        data = dict()
        data[Address.FIRST_NAME_KEY] = StringMock('first_name')
        data[Address.LAST_NAME_KEY] = StringMock('last_name')
        data[Address.STREET_KEY] = StringMock('street')
        data[Address.STREET_NUMBER_KEY] = StringMock('street_nr')
        data[Address.CITY_KEY] = StringMock('city')

        data_map = MapMock(data)
        Address(data_map)

    def test_can_construct_with_empty_map(self):
        data = dict()
        data_map = MapMock(data)
        Address(data_map)
        self.assertIn(Address.FIRST_NAME_KEY, data)
        self.assertIn(Address.LAST_NAME_KEY, data)
        self.assertIn(Address.STREET_KEY, data)
        self.assertIn(Address.STREET_NUMBER_KEY, data)
        self.assertIn(Address.CITY_KEY, data)

    def test_deletion_of_key_after_construction(self):
        data = dict()
        data[Address.FIRST_NAME_KEY] = StringMock('first_name')
        data[Address.LAST_NAME_KEY] = StringMock('last_name')
        data[Address.STREET_KEY] = StringMock('street')
        data[Address.STREET_NUMBER_KEY] = StringMock('street_nr')
        data[Address.CITY_KEY] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)
        del data[Address.FIRST_NAME_KEY]
        self.assertIsNone(address.first_name)

    def test_first_name_getter(self):
        data = dict()
        data[Address.FIRST_NAME_KEY] = StringMock('first_name')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.first_name, data[Address.FIRST_NAME_KEY].value)

    def test_first_name_setter(self):
        first_name = StringMock('first_name')
        address = Address()
        address.first_name = first_name
        first_name.parent = address
        self.assertEqual(address.first_name, first_name)

    def test_last_name_getter(self):
        data = dict()
        data[Address.LAST_NAME_KEY] = StringMock('last_name')

        data_map = MapMock(data)
        address = Address(data_map)
        self.assertEqual(address.last_name, data[Address.LAST_NAME_KEY].value)

    def test_last_name_setter(self):
        last_name = StringMock('last_name')
        address = Address()
        address.last_name = last_name
        last_name.parent = address
        self.assertEqual(address.last_name, last_name)

    def test_street_getter(self):
        data = dict()
        data[Address.STREET_KEY] = StringMock('street')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.street, data[Address.STREET_KEY].value)

    def test_street_setter(self):
        street = StringMock('street')
        address = Address()
        address.street = street
        street.parent = address
        self.assertEqual(address.street, street)

    def test_street_number_getter(self):
        data = dict()
        data[Address.STREET_NUMBER_KEY] = StringMock('street_nr')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(
            address.street_number,
            data[Address.STREET_NUMBER_KEY].value
        )

    def test_street_number_setter(self):
        street_number = StringMock('street_nr')
        address = Address()
        address.street_number = street_number
        street_number.parent = address
        self.assertEqual(address.street_number, street_number)

    def test_city_getter(self):
        data = dict()
        data[Address.CITY_KEY] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.city, data[Address.CITY_KEY].value)

    def test_city_setter(self):
        city = StringMock('city')
        address = Address()
        address.city = city
        city.parent = address
        self.assertEqual(address.city, city)

    def test_equal_equal_elements(self):
        data_map = MapMock({})
        comp = Address(data_map)
        equal_comp = Address(data_map)
        self.assertTrue(
            comp == equal_comp,
            msg='Equal elements are not equal'
        )

    def test_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({Address.FIRST_NAME_KEY: StructureMock('test')})
        comp = Address(data_map)
        other_comp = Address(other_data_map)
        self.assertFalse(
            comp == other_comp,
            msg='Unequal elements are equal'
        )

    def test_not_equal_equal_elements(self):
        data_map = MapMock({})
        comp = Address(data_map)
        equal_comp = Address(data_map)
        self.assertFalse(
            comp != equal_comp,
            msg='Equal elements are not equal'
        )

    def test_not_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({Address.FIRST_NAME_KEY: StructureMock('test')})
        comp = Address(data_map)
        other_comp = Address(other_data_map)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_to_string(self):
        data = dict()
        data[Address.FIRST_NAME_KEY] = StringMock('first_name')
        data[Address.LAST_NAME_KEY] = StringMock('last_name')
        data[Address.STREET_KEY] = StringMock('street')
        data[Address.STREET_NUMBER_KEY] = StringMock('street_nr')
        data[Address.CITY_KEY] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)
        expected = 'first_name last_name\nstreet street_nr\ncity'
        self.assertEqual(str(address), expected)

    def test_representation(self):
        data = dict()
        data[Address.FIRST_NAME_KEY] = StringMock('first_name')
        data[Address.LAST_NAME_KEY] = StringMock('last_name')
        data[Address.STREET_KEY] = StringMock('street')
        data[Address.STREET_NUMBER_KEY] = StringMock('street_nr')
        data[Address.CITY_KEY] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)
        expected = 'Address(first_name last_name, street street_nr, city)'
        self.assertEqual(repr(address), expected)
