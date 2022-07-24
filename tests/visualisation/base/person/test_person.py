import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from doubles.visualisation.double_base_type import BaseTypeMock
from src.visualisation.base.address.address import Address
from src.visualisation.base.image.image import Image
from src.visualisation.base.person.person import Person


class PersonTestSuite(unittest.TestCase):
    def test_can_construct(self):
        person = Person()
        self.assertIsNone(person.courtesy_title)
        self.assertEqual(person.first_name, '')
        self.assertIsNone(person.middle_name)
        self.assertEqual(person.last_name, '')
        self.assertIsNone(person.suffix)
        self.assertIsNone(person.gender)
        self.assertIsNone(person.sex)
        self.assertIsNone(person.marital_status)
        self.assertIsNone(person.nationality)


    def test_can_construct_with_map(self):
        data = dict()
        data[Person.COURTESY_TITLE_KEY] = StringMock(Person.COURTESY_TITLE_KEY)
        data[Person.FIRST_NAME_KEY] = StringMock(Person.FIRST_NAME_KEY)
        data[Person.MIDDLE_NAME_KEY] = StringMock(Person.MIDDLE_NAME_KEY)
        data[Person.LAST_NAME_KEY] = StringMock(Person.LAST_NAME_KEY)
        data[Person.SUFFIX_KEY] = StringMock(Person.SUFFIX_KEY)
        data[Person.GENDER_KEY] = StringMock(Person.GENDER_KEY)
        data[Person.SEX_KEY] = StringMock(Person.SEX_KEY)
        data[Person.MARITAL_STATUS_KEY] = StringMock(Person.MARITAL_STATUS_KEY)
        data[Person.NATIONALITY_KEY] = StringMock(Person.NATIONALITY_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertIsNotNone(person)

    def test_courtesy_title_getter(self):
        data = dict()
        data[Person.COURTESY_TITLE_KEY] = StringMock(Person.COURTESY_TITLE_KEY)

        data_map = MapMock(data)
        person = Person(data_map)

        self.assertEqual(person.courtesy_title, data[Person.COURTESY_TITLE_KEY].value)

    def test_courtesy_title_setter(self):
        courtesy_title = Person.COURTESY_TITLE_KEY
        person = Person()
        person.courtesy_title = courtesy_title
        self.assertEqual(person.courtesy_title, courtesy_title)

    def test_first_name_getter(self):
        data = dict()
        data[Person.FIRST_NAME_KEY] = StringMock(Person.FIRST_NAME_KEY)

        data_map = MapMock(data)
        person = Person(data_map)

        self.assertEqual(person.first_name, data[Person.FIRST_NAME_KEY].value)

    def test_first_name_setter(self):
        first_name = Person.FIRST_NAME_KEY
        person = Person()
        person.first_name = first_name
        self.assertEqual(person.first_name, first_name)

    def test_middle_name_getter(self):
        data = dict()
        data[Person.MIDDLE_NAME_KEY] = StringMock(Person.MIDDLE_NAME_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.middle_name, data[Person.MIDDLE_NAME_KEY].value)

    def test_middle_name_setter(self):
        middle_name = Person.MIDDLE_NAME_KEY
        person = Person()
        person.middle_name = middle_name
        self.assertEqual(person.middle_name, middle_name)

    def test_last_name_getter(self):
        data = dict()
        data[Person.LAST_NAME_KEY] = StringMock(Person.LAST_NAME_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.last_name, data[Person.LAST_NAME_KEY].value)

    def test_last_name_setter(self):
        last_name = Person.LAST_NAME_KEY
        person = Person()
        person.last_name = last_name
        self.assertEqual(person.last_name, last_name)

    def test_suffix_getter(self):
        data = dict()
        data[Person.SUFFIX_KEY] = StringMock(Person.SUFFIX_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.suffix, data[Person.SUFFIX_KEY].value)

    def test_suffix_setter(self):
        suffix = Person.SUFFIX_KEY
        person = Person()
        person.suffix = suffix
        self.assertEqual(person.suffix, suffix)

    def test_personal_photo_getter(self):
        data = dict()
        data[Person.PERSONAL_PHOTO_KEY] = MapMock({})

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.personal_photo.subject, data[Person.PERSONAL_PHOTO_KEY])

    def test_personal_photo_setter(self):
        personal_photo = BaseTypeMock(MapMock({
            Image.FILE_PATH_KEY: StringMock('Test'),
            Image.FILE_TYPE_KEY: StringMock('Test')
        }))
        person = Person()
        person.personal_photo = personal_photo
        self.assertEqual(person.personal_photo.subject.value, personal_photo.subject.value)

    def test_home_address_getter(self):
        data = dict()
        data[Person.HOME_ADDRESS_KEY] = MapMock({})

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.home_address.subject, data[Person.HOME_ADDRESS_KEY])

    def test_home_address_setter(self):
        home_address = BaseTypeMock(MapMock({
            Address.FIRST_NAME_KEY: StringMock('Test'),
            Address.LAST_NAME_KEY: StringMock('Test'),
            Address.STREET_KEY: StringMock('Test'),
            Address.STREET_NUMBER_KEY: StringMock('Test'),
            Address.CITY_KEY: StringMock('Test')
        }))
        person = Person()
        person.home_address = home_address
        self.assertEqual(person.home_address.subject.value, home_address.subject.value)

    def test_gender_getter(self):
        data = dict()
        data['gender'] = StringMock(Person.GENDER_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.gender, data[Person.GENDER_KEY].value)

    def test_gender_setter(self):
        gender = Person.GENDER_KEY
        person = Person()
        person.gender = gender
        self.assertEqual(person.gender, gender)

    def test_sex_getter(self):
        data = dict()
        data[Person.SEX_KEY] = StringMock(Person.SEX_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.sex, data[Person.SEX_KEY].value)

    def test_sex_setter(self):
        sex = Person.SEX_KEY
        person = Person()
        person.sex = sex
        self.assertEqual(person.sex, sex)

    def test_marital_status_getter(self):
        data = dict()
        data[Person.MARITAL_STATUS_KEY] = StringMock(Person.MARITAL_STATUS_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.marital_status, data[Person.MARITAL_STATUS_KEY].value)

    def test_marital_status_setter(self):
        marital_status = Person.MARITAL_STATUS_KEY
        person = Person()
        person.marital_status = marital_status
        self.assertEqual(person.marital_status, marital_status)

    def test_nationality_getter(self):
        data = dict()
        data[Person.NATIONALITY_KEY] = StringMock(Person.NATIONALITY_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.nationality, data[Person.NATIONALITY_KEY].value)

    def test_nationality_setter(self):
        nationality = Person.NATIONALITY_KEY
        person = Person()
        person.nationality = nationality
        self.assertEqual(person.nationality, nationality)

    def test_equal_equal_elements(self):
        data_map = MapMock({})
        comp = Person(data_map)
        equal_comp = Person(data_map)
        self.assertTrue(
            comp == equal_comp,
            msg='Equal elements are not equal'
        )

    def test_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({'first_name': StructureMock('test')})
        comp = Person(data_map)
        other_comp = Person(other_data_map)
        self.assertFalse(
            comp == other_comp,
            msg='Unequal elements are equal'
        )

    def test_not_equal_equal_elements(self):
        data_map = MapMock({})
        comp = Person(data_map)
        equal_comp = Person(data_map)
        self.assertFalse(
            comp != equal_comp,
            msg='Equal elements are not equal'
        )

    def test_not_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({'first_name': StructureMock('test')})
        comp = Person(data_map)
        other_comp = Person(other_data_map)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_to_string(self):
        data = dict()
        data[Person.COURTESY_TITLE_KEY] = StringMock(Person.COURTESY_TITLE_KEY)
        data[Person.FIRST_NAME_KEY] = StringMock(Person.FIRST_NAME_KEY)
        data[Person.MIDDLE_NAME_KEY] = StringMock(Person.MIDDLE_NAME_KEY)
        data[Person.LAST_NAME_KEY] = StringMock(Person.LAST_NAME_KEY)
        data[Person.SUFFIX_KEY] = StringMock(Person.SUFFIX_KEY)
        data[Person.GENDER_KEY] = StringMock(Person.GENDER_KEY)
        data[Person.SEX_KEY] = StringMock(Person.SEX_KEY)
        data[Person.MARITAL_STATUS_KEY] = StringMock(Person.MARITAL_STATUS_KEY)
        data[Person.NATIONALITY_KEY] = StringMock(Person.NATIONALITY_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        expected = f'{Person.COURTESY_TITLE_KEY} {Person.FIRST_NAME_KEY} ' \
                   f'{Person.MIDDLE_NAME_KEY} {Person.LAST_NAME_KEY} ' \
                   f'{Person.SUFFIX_KEY}\n{Person.GENDER_KEY}\n{Person.SEX_KEY}\n' \
                   f'{Person.MARITAL_STATUS_KEY}\n{Person.NATIONALITY_KEY}'
        self.assertEqual(str(person), expected)

    def test_representation(self):
        data = dict()
        data[Person.COURTESY_TITLE_KEY] = StringMock(Person.COURTESY_TITLE_KEY)
        data[Person.FIRST_NAME_KEY] = StringMock(Person.FIRST_NAME_KEY)
        data[Person.MIDDLE_NAME_KEY] = StringMock(Person.MIDDLE_NAME_KEY)
        data[Person.LAST_NAME_KEY] = StringMock(Person.LAST_NAME_KEY)
        data[Person.SUFFIX_KEY] = StringMock(Person.SUFFIX_KEY)
        data[Person.GENDER_KEY] = StringMock(Person.GENDER_KEY)
        data[Person.SEX_KEY] = StringMock(Person.SEX_KEY)
        data[Person.MARITAL_STATUS_KEY] = StringMock(Person.MARITAL_STATUS_KEY)
        data[Person.NATIONALITY_KEY] = StringMock(Person.NATIONALITY_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        expected = f'Person({Person.COURTESY_TITLE_KEY} ' \
                   f'{Person.FIRST_NAME_KEY} {Person.MIDDLE_NAME_KEY}' \
                   f' {Person.LAST_NAME_KEY} ' \
                   f'{Person.SUFFIX_KEY}, {Person.GENDER_KEY}, ' \
                   f'{Person.SEX_KEY}, ' \
                   f'{Person.MARITAL_STATUS_KEY}, {Person.NATIONALITY_KEY})'
        self.assertEqual(repr(person), expected)
