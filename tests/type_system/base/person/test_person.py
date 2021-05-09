import unittest

from doubles.structure.double_info import InfoMock
from doubles.structure.double_map import MapMock
from doubles.structure.double_string import StringMock
from src.type_system.base.person.person import Person


class PersonTestSuite(unittest.TestCase):
    def test_can_construct(self):
        person = Person()
        self.assertIsNone(person.courtesy_title)
        self.assertIsNone(person.first_name)
        self.assertIsNone(person.middle_name)
        self.assertIsNone(person.last_name)
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
        Person(data_map)

    def test_courtesy_title_getter(self):
        data = dict()
        data[Person.COURTESY_TITLE_KEY] = StringMock(Person.COURTESY_TITLE_KEY)

        data_map = MapMock(data)
        person = Person(data_map)

        self.assertEqual(person.courtesy_title, data[Person.COURTESY_TITLE_KEY])

    def test_courtesy_title_setter(self):
        courtesy_title = StringMock(Person.COURTESY_TITLE_KEY)
        person = Person()
        person.courtesy_title = courtesy_title
        courtesy_title.parent = person
        self.assertEqual(person.courtesy_title, courtesy_title)

    def test_first_name_getter(self):
        data = dict()
        data[Person.FIRST_NAME_KEY] = StringMock(Person.FIRST_NAME_KEY)

        data_map = MapMock(data)
        person = Person(data_map)

        self.assertEqual(person.first_name, data[Person.FIRST_NAME_KEY])

    def test_first_name_setter(self):
        first_name = StringMock(Person.FIRST_NAME_KEY)
        person = Person()
        person.first_name = first_name
        first_name.parent = person
        self.assertEqual(person.first_name, first_name)

    def test_middle_name_getter(self):
        data = dict()
        data[Person.MIDDLE_NAME_KEY] = StringMock(Person.MIDDLE_NAME_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.middle_name, data[Person.MIDDLE_NAME_KEY])

    def test_middle_name_setter(self):
        middle_name = StringMock(Person.MIDDLE_NAME_KEY)
        person = Person()
        person.middle_name = middle_name
        middle_name.parent = person
        self.assertEqual(person.middle_name, middle_name)

    def test_last_name_getter(self):
        data = dict()
        data[Person.LAST_NAME_KEY] = StringMock(Person.LAST_NAME_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.last_name, data[Person.LAST_NAME_KEY])

    def test_last_name_setter(self):
        last_name = StringMock(Person.LAST_NAME_KEY)
        person = Person()
        person.last_name = last_name
        last_name.parent = person
        self.assertEqual(person.last_name, last_name)

    def test_suffix_getter(self):
        data = dict()
        data[Person.SUFFIX_KEY] = StringMock(Person.SUFFIX_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.suffix, data[Person.SUFFIX_KEY])

    def test_suffix_setter(self):
        suffix = StringMock(Person.SUFFIX_KEY)
        person = Person()
        person.suffix = suffix
        suffix.parent = person
        self.assertEqual(person.suffix, suffix)

    def test_gender_getter(self):
        data = dict()
        data['gender'] = StringMock(Person.GENDER_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.gender, data[Person.GENDER_KEY])

    def test_gender_setter(self):
        gender = StringMock(Person.GENDER_KEY)
        person = Person()
        person.gender = gender
        gender.parent = person
        self.assertEqual(person.gender, gender)

    def test_sex_getter(self):
        data = dict()
        data[Person.SEX_KEY] = StringMock(Person.SEX_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.sex, data[Person.SEX_KEY])

    def test_sex_setter(self):
        sex = StringMock(Person.SEX_KEY)
        person = Person()
        person.sex = sex
        sex.parent = person
        self.assertEqual(person.sex, sex)

    def test_marital_status_getter(self):
        data = dict()
        data[Person.MARITAL_STATUS_KEY] = StringMock(Person.MARITAL_STATUS_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.marital_status, data[Person.MARITAL_STATUS_KEY])

    def test_marital_status_setter(self):
        marital_status = StringMock(Person.MARITAL_STATUS_KEY)
        person = Person()
        person.marital_status = marital_status
        marital_status.parent = person
        self.assertEqual(person.marital_status, marital_status)

    def test_nationality_getter(self):
        data = dict()
        data[Person.NATIONALITY_KEY] = StringMock(Person.NATIONALITY_KEY)

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.nationality, data[Person.NATIONALITY_KEY])

    def test_nationality_setter(self):
        nationality = StringMock(Person.NATIONALITY_KEY)
        person = Person()
        person.nationality = nationality
        nationality.parent = person
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
        other_data_map = MapMock({'first_name': InfoMock('test')})
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
        other_data_map = MapMock({'first_name': InfoMock('test')})
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
