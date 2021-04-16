import unittest
from doubles.structure.info import InfoMock
from doubles.structure.map import MapMock
from doubles.structure.string import StringMock
from src.type_system.base.image.image import Image


class ImageTestSuite(unittest.TestCase):
    def test_can_construct(self):
        image = Image()
        self.assertEqual(image.file_path, '')
        self.assertTrue(image.file_type.startswith('image/'))

    def test_can_construct_with_map(self):
        data = dict()
        data[Image.FILE_PATH_KEY] = StringMock('file_path')
        data[Image.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        Image(data_map)

    def test_can_construct_with_empty_map(self):
        data = dict()
        data_map = MapMock(data)
        Image(data_map)
        self.assertIn(Image.FILE_PATH_KEY, data)
        self.assertIn(Image.FILE_TYPE_KEY, data)
        self.assertTrue(data[Image.FILE_TYPE_KEY].startswith('image/'))

    def test_deletion_of_key_after_construction(self):
        data = dict()
        data[Image.FILE_PATH_KEY] = StringMock('file_path')
        data[Image.FILE_TYPE_KEY] = StringMock('image/mock')

        data_map = MapMock(data)
        image = Image(data_map)
        del data[Image.FILE_PATH_KEY]
        self.assertIsNone(image.file_path)

    def test_file_path_getter(self):
        data = dict()
        data[Image.FILE_PATH_KEY] = StringMock('file_path')

        data_map = MapMock(data)
        image = Image(data_map)

        self.assertEqual(image.file_path, data[Image.FILE_PATH_KEY].value)

    def test_file_path_setter(self):
        file_path = StringMock('file_path')
        image = Image()
        image.file_path = file_path
        file_path.parent = image
        self.assertEqual(image.file_path, file_path)

    def test_file_type_getter(self):
        data = dict()
        data[Image.FILE_TYPE_KEY] = StringMock('image/mock')

        data_map = MapMock(data)
        image = Image(data_map)
        self.assertEqual(image.file_type, data[Image.FILE_TYPE_KEY].value)

    def test_file_type_setter(self):
        file_type = StringMock('file_type')
        image = Image()
        image.file_type = file_type
        file_type.parent = image
        self.assertEqual(image.file_type, file_type)

    def test_equal_equal_elements(self):
        data_map = MapMock({})
        comp = Image(data_map)
        equal_comp = Image(data_map)
        self.assertTrue(
            comp == equal_comp,
            msg='Equal elements are not equal'
        )

    def test_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({Image.FILE_PATH_KEY: InfoMock('test')})
        comp = Image(data_map)
        other_comp = Image(other_data_map)
        self.assertFalse(
            comp == other_comp,
            msg='Unequal elements are equal'
        )

    def test_not_equal_equal_elements(self):
        data_map = MapMock({})
        comp = Image(data_map)
        equal_comp = Image(data_map)
        self.assertFalse(
            comp != equal_comp,
            msg='Equal elements are not equal'
        )

    def test_not_equal_unequal_elements(self):
        data_map = MapMock({})
        other_data_map = MapMock({Image.FILE_PATH_KEY: InfoMock('test')})
        comp = Image(data_map)
        other_comp = Image(other_data_map)
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_to_string(self):
        data = dict()
        data[Image.FILE_PATH_KEY] = StringMock('file_path')
        data[Image.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        image = Image(data_map)
        expected = 'file_path (file_type)'
        self.assertEqual(str(image), expected)

    def test_representation(self):
        data = dict()
        data[Image.FILE_PATH_KEY] = StringMock('file_path')
        data[Image.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        image = Image(data_map)
        expected = 'Image(file_path, file_type)'
        self.assertEqual(repr(image), expected)
