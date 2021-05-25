import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.base.image.image import Image
from src.visualisation.base.image.image_view_model import ImageViewModel


class ImageViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ImageViewModel(InterpretationMock(MapMock()))

    def test_can_get_file_path(self):
        view_model = ImageViewModel(InterpretationMock(MapMock()))
        self.assertEqual(view_model.file_path, '')

    def test_file_path_getter(self):
        data = dict()
        data[Image.FILE_PATH_KEY] = StringMock('file_path')

        data_map = MapMock(data)
        view_model = ImageViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.file_path, data[Image.FILE_PATH_KEY].value)

    def test_file_path_setter(self):
        file_path = 'file_path'
        view_model = ImageViewModel(InterpretationMock(MapMock()))
        view_model.file_path = file_path
        self.assertEqual(view_model.file_path, file_path)

    def test_can_get_file_type(self):
        view_model = ImageViewModel(InterpretationMock(MapMock()))
        self.assertTrue(view_model.file_type.startswith('image/'))

    def test_file_type_getter(self):
        data = dict()
        data[Image.FILE_TYPE_KEY] = StringMock('file_type')

        data_map = MapMock(data)
        view_model = ImageViewModel(InterpretationMock(data_map))
        self.assertEqual(view_model.file_type, data[Image.FILE_TYPE_KEY].value)

    def test_file_type_setter(self):
        file_type = 'file_type'
        view_model = ImageViewModel(InterpretationMock(MapMock()))
        view_model.file_type = file_type
        self.assertEqual(view_model.file_type, file_type)
