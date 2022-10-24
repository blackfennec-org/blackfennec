import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec.interpretation.specification import Specification
from base.file.file_view import FileView
from base.file.file_view_factory import FileViewFactory


class FileViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        FileViewFactory()

    def test_can_create_file_view(self):
        factory = FileViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, FileView)

    def test_satisfies_default(self):
        factory = FileViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = FileViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
