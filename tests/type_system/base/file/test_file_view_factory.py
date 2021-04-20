import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.map import MapMock
from src.interpretation.specification import Specification
from src.type_system.base.file.file_view import FileView
from src.type_system.base.file.file_view_factory import FileViewFactory


class FileViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileViewFactory()

    def test_can_create_file_view(self):
        factory = FileViewFactory()
        view = factory.create(InterpretationMock(MapMock()), Specification())
        self.assertIsInstance(view, FileView)

    def test_satisfies_default(self):
        factory = FileViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = FileViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
