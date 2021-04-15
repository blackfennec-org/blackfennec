import unittest

from doubles.core import MapMock
from doubles.core.interpretation import InterpretationMock
from src.base.types.file.file_view import FileView
from src.base.types.file.file_view_factory import FileViewFactory


class FileViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileViewFactory()

    def test_can_create_file_view(self):
        factory = FileViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, FileView)
