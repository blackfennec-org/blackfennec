import unittest
from doubles.core import MapMock, StringMock, InfoMock
from src.base.types.person.person import Person


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
        data['courtesy_title'] = StringMock('courtesy_title')
        data['first_name'] = StringMock('first_name')
        data['middle_name'] = StringMock('middle_name')
        data['last_name'] = StringMock('last_name')
        data['suffix'] = StringMock('suffix')
        data['gender'] = StringMock('gender')
        data['sex'] = StringMock('sex')
        data['marital_status'] = StringMock('marital_status')
        data['nationality'] = StringMock('nationality')

        data_map = MapMock(data)
        Person(data_map)

    def test_courtesy_title_getter(self):
        data = dict()
        data['courtesy_title'] = StringMock('courtesy_title')

        data_map = MapMock(data)
        person = Person(data_map)

        self.assertEqual(person.courtesy_title, data['courtesy_title'])

    def test_courtesy_title_setter(self):
        courtesy_title = StringMock('courtesy_title')
        person = Person()
        person.courtesy_title = courtesy_title
        courtesy_title.parent = person
        self.assertEqual(person.first_name, courtesy_title)

    def test_first_name_getter(self):
        data = dict()
        data['first_name'] = StringMock('first_name')

        data_map = MapMock(data)
        person = Person(data_map)

        self.assertEqual(person.first_name, data['first_name'])

    def test_first_name_setter(self):
        first_name = StringMock('first_name')
        person = Person()
        person.first_name = first_name
        first_name.parent = person
        self.assertEqual(person.first_name, first_name)

    def test_middle_name_getter(self):
        data = dict()
        data['middle_name'] = StringMock('middle_name')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.middle_name, data['middle_name'])

    def test_middle_name_setter(self):
        middle_name = StringMock('middle_name')
        person = Person()
        person.middle_name = middle_name
        middle_name.parent = person
        self.assertEqual(person.middle_name, middle_name)

    def test_last_name_getter(self):
        data = dict()
        data['last_name'] = StringMock('last_name')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.last_name, data['last_name'])

    def test_last_name_setter(self):
        last_name = StringMock('last_name')
        person = Person()
        person.last_name = last_name
        last_name.parent = person
        self.assertEqual(person.last_name, last_name)

    def test_suffix_getter(self):
        data = dict()
        data['suffix'] = StringMock('suffix')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.suffix, data['suffix'])

    def test_suffix_setter(self):
        suffix = StringMock('suffix')
        person = Person()
        person.suffix = suffix
        suffix.parent = person
        self.assertEqual(person.suffix, suffix)

    def test_gender_getter(self):
        data = dict()
        data['gender'] = StringMock('gender')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.gender, data['gender'])

    def test_gender_setter(self):
        gender = StringMock('gender')
        person = Person()
        person.gender = gender
        gender.parent = person
        self.assertEqual(person.gender, gender)

    def test_sex_getter(self):
        data = dict()
        data['sex'] = StringMock('sex')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.sex, data['sex'])

    def test_sex_setter(self):
        sex = StringMock('sex')
        person = Person()
        person.sex = sex
        sex.parent = person
        self.assertEqual(person.sex, sex)

    def test_marital_status_getter(self):
        data = dict()
        data['marital_status'] = StringMock('marital_status')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.marital_status, data['marital_status'])

    def test_marital_status_setter(self):
        marital_status = StringMock('marital_status')
        person = Person()
        person.marital_status = marital_status
        marital_status.parent = person
        self.assertEqual(person.marital_status, marital_status)

    def test_nationality_getter(self):
        data = dict()
        data['nationality'] = StringMock('nationality')

        data_map = MapMock(data)
        person = Person(data_map)
        self.assertEqual(person.nationality, data['nationality'])

    def test_nationality_setter(self):
        nationality = StringMock('nationality')
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
        data['courtesy_title'] = StringMock('courtesy_title')
        data['first_name'] = StringMock('first_name')
        data['middle_name'] = StringMock('middle_name')
        data['last_name'] = StringMock('last_name')
        data['suffix'] = StringMock('suffix')
        data['gender'] = StringMock('gender')
        data['sex'] = StringMock('sex')
        data['marital_status'] = StringMock('marital_state')
        data['nationality'] = StringMock('nationality')

        data_map = MapMock(data)
        person = Person(data_map)
        expected = 'courtesy_title first_name middle_name last_name suffix\ngender\nsex\nmarital_status\nnationality'
        self.assertEqual(str(person), expected)

    def test_representation(self):
        data = dict()
        data['courtesy_title'] = StringMock('courtesy_title')
        data['first_name'] = StringMock('first_name')
        data['middle_name'] = StringMock('middle_name')
        data['last_name'] = StringMock('last_name')
        data['suffix'] = StringMock('suffix')
        data['gender'] = StringMock('gender')
        data['sex'] = StringMock('sex')
        data['marital_status'] = StringMock('marital_state')
        data['nationality'] = StringMock('nationality')

        data_map = MapMock(data)
        person = Person(data_map)
        expected = 'Person(courtesy_title first_name middle_name last_name suffix, gender, sex, marital_status, nationality)'
        self.assertEqual(repr(person), expected)
