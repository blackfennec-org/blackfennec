import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.person.person_view_model import PersonViewModel


class PersonViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        PersonViewModel(InterpretationMock(MapMock()))

    def test_can_get_courtesy_title(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.courtesy_title, None)

    def test_courtesy_title_getter(self):
        data = dict()
        data['courtesy_title'] = StringMock('courtesy_title')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.courtesy_title, data['courtesy_title'].value)

    def test_courtesy_title_setter(self):
        courtesy_title = StringMock('courtesy_title')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.courtesy_title = courtesy_title
        courtesy_title.parent = view_model
        self.assertEqual(view_model.courtesy_title, courtesy_title)

    def test_can_get_first_name(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.first_name, '')

    def test_first_name_getter(self):
        data = dict()
        data['first_name'] = StringMock('first_name')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.first_name, data['first_name'].value)

    def test_first_name_setter(self):
        first_name = StringMock('first_name')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.first_name = first_name
        first_name.parent = view_model
        self.assertEqual(view_model.first_name, first_name)

    def test_can_get_middle_name(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertIsNone(view_model.middle_name)

    def test_middle_name_getter(self):
        data = dict()
        data['middle_name'] = StringMock('middle_name')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.middle_name, data['middle_name'].value)

    def test_middle_name_setter(self):
        middle_name = StringMock('middle_name')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.middle_name = middle_name
        middle_name.parent = view_model
        self.assertEqual(view_model.middle_name, middle_name)

    def test_can_get_last_name(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.last_name, '')

    def test_last_name_getter(self):
        data = dict()
        data['last_name'] = StringMock('last_name')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.last_name, data['last_name'].value)

    def test_last_name_setter(self):
        last_name = StringMock('last_name')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.last_name = last_name
        last_name.parent = view_model
        self.assertEqual(view_model.last_name, last_name)

    def test_can_get_suffix(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertIsNone(view_model.suffix)

    def test_suffix_getter(self):
        data = dict()
        data['suffix'] = StringMock('suffix')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.suffix, data['suffix'].value)

    def test_suffix_setter(self):
        suffix = StringMock('suffix')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.suffix = suffix
        suffix.parent = view_model
        self.assertEqual(view_model.suffix, suffix)

    def test_can_get_gender(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertIsNone(view_model.gender)

    def test_gender_getter(self):
        data = dict()
        data['gender'] = StringMock('gender')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.gender, data['gender'].value)

    def test_gender_setter(self):
        gender = StringMock('gender')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.gender = gender
        gender.parent = view_model
        self.assertEqual(view_model.gender, gender)

    def test_can_get_sex(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertIsNone(view_model.sex)

    def test_sex_getter(self):
        data = dict()
        data['sex'] = StringMock('sex')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.sex, data['sex'].value)

    def test_sex_setter(self):
        sex = StringMock('sex')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.sex = sex
        sex.parent = view_model
        self.assertEqual(view_model.sex, sex)

    def test_can_get_marital_status(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertIsNone(view_model.marital_status)

    def test_marital_status_getter(self):
        data = dict()
        data['marital_status'] = StringMock('marital_status')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.marital_status, data['marital_status'].value)

    def test_marital_status_setter(self):
        marital_status = StringMock('marital_status')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.marital_status = marital_status
        marital_status.parent = view_model
        self.assertEqual(view_model.marital_status, marital_status)

    def test_can_get_nationality(self):
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        self.assertIsNone(view_model.nationality)

    def test_nationality_getter(self):
        data = dict()
        data['nationality'] = StringMock('nationality')

        data_map = MapMock(data)
        view_model = PersonViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.nationality, data['nationality'].value)

    def test_nationality_setter(self):
        nationality = StringMock('nationality')
        view_model = PersonViewModel(InterpretationMock(MapMock()))
        view_model.nationality = nationality
        nationality.parent = view_model
        self.assertEqual(view_model.nationality, nationality)




