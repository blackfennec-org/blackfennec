import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_string import StringMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.core.string.string_view import StringView
from src.visualisation.core.string.string_preview import StringPreview
from src.visualisation.core.string.string_view_factory import StringViewFactory


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
