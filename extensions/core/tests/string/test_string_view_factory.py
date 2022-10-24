import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec.interpretation.specification import Specification
from core.string.string_view import StringView
from core.string.string_preview import StringPreview
from core.string.string_view_factory import StringViewFactory


class StringViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewFactory()

    def test_can_create_string_view(self):
        factory = StringViewFactory()
        view = factory.create(InterpretationMock(StringMock()))
        self.assertIsInstance(view, StringView)

    def test_can_create_string_preview(self):
        factory = StringViewFactory()
        specification = Specification(request_preview=True)
        interpretation = InterpretationMock(StringMock(), specification=specification)
        view = factory.create(interpretation)
        self.assertIsInstance(view, StringPreview)

    def test_satisfies_default(self):
        factory = StringViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = StringViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
