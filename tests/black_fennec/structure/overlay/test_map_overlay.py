import unittest
from typing import Optional

from uri import URI

from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.encapsulation_base import _create_generic_class
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.overlay.map_overlay import MapOverlay
from src.black_fennec.structure.overlay.overlay_base import OverlayBase
from src.black_fennec.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root


class MapOverlayTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = OverlayFactoryVisitor()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_overlay: Optional[MapOverlay] = MapOverlay(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_overlay: Optional[MapOverlay] = None

    def test_can_create(self):
        self.assertIsNotNone(self.map_overlay)

    def test_get_item_with_reference(self):
        key = 'test'
        value = InfoMock('test_value')
        resolving_service = JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, URI('0'))
        subject = Map({key: ref})
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.visitor,
            subject
        )
        get = map_overlay[key].subject
        self.assertEqual(get, value)

    def test_get_item(self):
        key = 'test'
        value = InfoMock('test_value')
        subject = Map({key: value})
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.visitor,
            subject
        )
        get = map_overlay[key].subject
        self.assertEqual(get, value)

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = InfoMock('test_value')
        template_class = _create_generic_class(OverlayBase, Info)
        encapsulated = template_class(self.visitor, value)
        self.map_overlay[key] = encapsulated
        self.assertEqual(value, self.map_overlay[key].subject)

    def test_set_item_map_already_encapsulated(self):
        key = 'test'
        value = Map()
        encapsulated = MapOverlay(self.visitor, value)
        self.map_overlay[key] = encapsulated
        self.assertEqual(value, self.map_overlay[key].subject)

    def test_can_get_repr(self):
        representation: str = self.map_overlay.__repr__()
        self.assertTrue(representation.startswith('MapOverlay('))
