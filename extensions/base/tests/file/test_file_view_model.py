import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_string import StringMock
from base.file.file import File
from base.file.file_view_model import FileViewModel


class FileViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileViewModel(InterpretationMock(MapMock()))

    def test_can_get_file_path(self):
        view_model = FileViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.file_path, '')

    def test_file_path_getter(self):
        data = dict()
        data[File.FILE_PATH_KEY] = StringMock('file_path')

        data_map = MapMock(data)
        view_model = FileViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.file_path, data[File.FILE_PATH_KEY].value)

    def test_file_path_setter(self):
        file_path = 'file_path'
        view_model = FileViewModel(InterpretationMock(MapMock()))
        view_model.file_path = file_path
        self.assertEqual(view_model.file_path, file_path)

    def test_can_get_file_type(self):
        view_model = FileViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.file_type, '')

    def test_file_type_getter(self):
        data = dict()
        data[File.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        view_model = FileViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.file_type, data[File.FILE_TYPE_KEY].value)

    def test_file_type_setter(self):
        file_type = 'file_type'
        view_model = FileViewModel(InterpretationMock(MapMock()))
        view_model.file_type = file_type
        self.assertEqual(view_model.file_type, file_type)
