import unittest
from doubles.core import MapMock, StringMock, InfoMock
from src.base.types.address.address import Address


class AddressTestSuite(unittest.TestCase):
    def test_can_construct(self):
        address = Address()
        self.assertFalse(address.first_name)
        self.assertFalse(address.last_name)
        self.assertFalse(address.street)
        self.assertFalse(address.street_number)
        self.assertFalse(address.city)

    def test_can_construct_with_map(self):
        data = dict()
        data['first_name'] = StringMock('first_name')
        data['last_name'] = StringMock('last_name')
        data['street'] = StringMock('street')
        data['street_nr'] = StringMock('street_nr')
        data['city'] = StringMock('city')

        data_map = MapMock(data)
        Address(data_map)

    def test_first_name_getter(self):
        data = dict()
        data['first_name'] = StringMock('first_name')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.first_name, data['first_name'])

    def test_first_name_setter(self):
        first_name = StringMock('first_name')
        address = Address()
        address.first_name = first_name
        first_name.parent = address
        self.assertEqual(address.first_name, first_name)

    def test_last_name_getter(self):
        data = dict()
        data['last_name'] = StringMock('last_name')

        data_map = MapMock(data)
        address = Address(data_map)
        self.assertEqual(address.last_name, data['last_name'])

    def test_last_name_setter(self):
        last_name = StringMock('last_name')
        address = Address()
        address.last_name = last_name
        last_name.parent = address
        self.assertEqual(address.last_name, last_name)

    def test_street_getter(self):
        data = dict()
        data['street'] = StringMock('street')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.street, data['street'])

    def test_street_setter(self):
        street = StringMock('street')
        address = Address()
        address.street = street
        street.parent = address
        self.assertEqual(address.street, street)

    def test_street_number_getter(self):
        data = dict()
        data['street_nr'] = StringMock('street_nr')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.street_number, data['street_nr'])

    def test_street_number_setter(self):
        street_number = StringMock('street_nr')
        address = Address()
        address.street_number = street_number
        street_number.parent = address
        self.assertEqual(address.street_number, street_number)

    def test_city_getter(self):
        data = dict()
        data['city'] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)

        self.assertEqual(address.city, data['city'])

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
        other_data_map = MapMock({'first_name': InfoMock('test')})
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
        other_data_map = MapMock({'first_name': InfoMock('test')})
        comp = Address(data_map)
        other_comp = Address(other_data_map)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_to_string(self):
        data = dict()
        data['first_name'] = StringMock('first_name')
        data['last_name'] = StringMock('last_name')
        data['street'] = StringMock('street')
        data['street_nr'] = StringMock('street_nr')
        data['city'] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)
        expected = 'first_name last_name\nstreet street_nr\ncity'
        self.assertEqual(str(address), expected)

    def test_representation(self):
        data = dict()
        data['first_name'] = StringMock('first_name')
        data['last_name'] = StringMock('last_name')
        data['street'] = StringMock('street')
        data['street_nr'] = StringMock('street_nr')
        data['city'] = StringMock('city')

        data_map = MapMock(data)
        address = Address(data_map)
        expected = 'Address(first_name last_name, street street_nr, city)'
        self.assertEqual(repr(address), expected)
