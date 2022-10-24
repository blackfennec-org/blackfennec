import unittest
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_string import StringMock
from base.file.file import File


class FileTestSuite(unittest.TestCase):
    def test_can_construct(self):
        file = File()
        self.assertEqual(file.file_path, '')
        self.assertEqual(file.file_type, '')

    def test_can_construct_with_map(self):
        data = dict()
        data[File.FILE_PATH_KEY] = StringMock('file_path')
        data[File.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        file = File(data_map)

        self.assertIsNotNone(file)

    def test_can_construct_with_empty_map(self):
        data = dict()
        data_map = MapMock(data)
        file = File(data_map)

        self.assertIsNotNone(file)

    def test_deletion_of_key_after_construction(self):
        data = dict()
        data[File.FILE_PATH_KEY] = StringMock('file_path')
        data[File.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        file = File(data_map)
        del data[File.FILE_PATH_KEY]
        self.assertIsNone(file.file_path)

    def test_file_path_getter(self):
        data = dict()
        data[File.FILE_PATH_KEY] = StringMock('file_path')

        data_map = MapMock(data)
        file = File(data_map)

        self.assertEqual(file.file_path, data[File.FILE_PATH_KEY].value)

    def test_file_path_setter(self):
        file_path = StringMock('file_path')
        file = File()
        file.file_path = file_path
        file_path.parent = file
        self.assertEqual(file.file_path, file_path)

    def test_file_type_getter(self):
        data = dict()
        data[File.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        file = File(data_map)
        self.assertEqual(file.file_type, data[File.FILE_TYPE_KEY].value)

    def test_file_type_setter(self):
        file_type = StringMock('file_type')
        file = File()
        file.file_type = file_type
        file_type.parent = file
        self.assertEqual(file.file_type, file_type)


    def test_not_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({File.FILE_PATH_KEY: StructureMock('test')})
        comp = File(data_map)
        other_comp = File(other_data_map)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_representation(self):
        data = dict()
        data[File.FILE_PATH_KEY] = StringMock('file_path')
        data[File.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        file = File(data_map)
        expected = 'File(file_path, file_type)'
        self.assertEqual(repr(file), expected)
