import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.double_map import MapMock
from doubles.structure.overlay.double_overlay_factory import OverlayFactoryMock
from doubles.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.info import Info
from src.structure.map import Map
from src.structure.reference import Reference
from src.structure.root import Root
from src.structure.overlay.map_overlay import MapOverlay
from src.structure.overlay.overlay_factory import _get_overlay_class


class MapOverlayTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = OverlayFactoryMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_overlay: Optional[MapOverlay] = MapOverlay(self.subject, self.factory)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.map_overlay: Optional[MapOverlay] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.map_overlay.subject, self.subject)

    def test_get_item(self):
        key = 'test'
        value = InfoMock('test_value')
        self.subject[key] = value
        self.factory._create_return = value
        map_overlay: Optional[MapOverlay] = MapOverlay(self.subject, self.factory)
        get = map_overlay[key]
        self.assertEqual(get, value)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_set_item(self):
        key = 'test'
        value = InfoMock('test_value')
        self.factory._create_return = value
        self.map_overlay[key] = value
        self.assertEqual(value, self.map_overlay[key])

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = InfoMock('test_value')
        overlay_class = _get_overlay_class(Info)
        encapsulated = overlay_class(value, self.factory)
        self.factory._create_return = encapsulated
        self.factory._create_return = value
        self.map_overlay[key] = encapsulated
        self.assertEqual(value, self.map_overlay[key])

    def test_get_children(self):
        key = 'test'
        value = InfoMock('test_value')
        self.subject[key] = value
        self.factory._create_return = value
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.subject,
            self.factory
        )
        children = map_overlay.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_children_with_reference(self):
        key = 'test'
        value = InfoMock('test_value')
        resolving_service = \
            JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, '0')
        self.subject[key] = ref
        self.factory._create_return = value
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.subject,
            self.factory
        )
        children = map_overlay.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_empty_children(self):
        children = self.map_overlay.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.factory._create_calls, 0)

    def test_can_get_repr(self):
        representation: str = self.map_overlay.__repr__()
        self.assertTrue(representation.startswith('MapOverlay('))
