import unittest
from typing import Optional

from doubles.structure.double_info import InfoMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.map import Map
from src.structure.overlay.map_overlay import MapOverlay
from src.structure.reference import Reference
from src.structure.root import Root


class MapOverlayTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_overlay: Optional[MapOverlay] = MapOverlay(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_overlay: Optional[MapOverlay] = None

    def test_can_create(self):
        pass

    def test_get_item_with_reference(self):
        key = 'test'
        value = InfoMock('test_value')
        resolving_service = JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, '0')
        subject = Map({key: ref})
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.visitor,
            subject
        )
        get = map_overlay[key]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_item(self):
        key = 'test'
        value = InfoMock('test_value')
        subject = Map({key: value})
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.visitor,
            subject
        )
        get = map_overlay[key]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_can_get_repr(self):
        representation: str = self.map_overlay.__repr__()
        self.assertTrue(representation.startswith('MapOverlay('))
