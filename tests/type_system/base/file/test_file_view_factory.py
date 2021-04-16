import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.map import MapMock
from src.type_system.base.file.file_view import FileView
from src.type_system.base.file.file_view_factory import FileViewFactory


class FileViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileViewFactory()

    def test_can_create_file_view(self):
        factory = FileViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, FileView)
