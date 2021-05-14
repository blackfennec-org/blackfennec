import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_string import StringMock
from src.interpretation.specification import Specification
from src.type_system.core.string.string_view import StringView
from src.type_system.core.string.string_preview import StringPreview
from src.type_system.core.string.string_view_factory import StringViewFactory


class StringViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewFactory()

    def test_can_create_string_view(self):
        factory = StringViewFactory()
        specification = Specification()
        view = factory.create(InterpretationMock(StringMock()), specification)
        self.assertIsInstance(view, StringView)

    def test_can_create_string_preview(self):
        factory = StringViewFactory()
        specification = Specification(request_preview=True)
        view = factory.create(InterpretationMock(StringMock()), specification)
        self.assertIsInstance(view, StringPreview)

    def test_satisfies_default(self):
        factory = StringViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = StringViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
