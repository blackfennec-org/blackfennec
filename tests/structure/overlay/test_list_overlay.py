import unittest
from typing import Optional

from doubles.structure.double_info import InfoMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.info import Info
from src.structure.list import List
from src.structure.reference import Reference
from src.structure.root import Root
from src.structure.overlay.list_overlay import ListOverlay


class ListOverlayTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_overlay: Optional[ListOverlay] = ListOverlay(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.list_overlay: Optional[ListOverlay] = None

    def test_can_create(self):
        pass

    def test_get_item_with_reference(self):
        value = InfoMock('test_value')
        resolving_service = JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, '0')
        subject = List([ref])
        list_overlay: Optional[ListOverlay] = ListOverlay(
            self.visitor,
            subject
        )
        get = list_overlay[0]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        list_overlay: Optional[ListOverlay] = ListOverlay(
            self.visitor,
            subject
        )
        get = list_overlay[0]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_can_get_repr(self):
        representation: str = self.list_overlay.__repr__()
        self.assertTrue(representation.startswith('ListOverlay('))
