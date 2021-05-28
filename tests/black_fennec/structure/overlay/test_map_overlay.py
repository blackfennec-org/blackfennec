import unittest
from typing import Optional

from uri import URI

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.overlay.map_overlay import MapOverlay
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root


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
        value = StructureMock('test_value')
        resolving_service = JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, URI('0'))
        subject = Map({key: ref})
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.visitor,
            subject
        )
        get = map_overlay.value[key]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.structure, value)
        self.assertEqual(self.visitor.visit_structure_count, 1)

    def test_get_item(self):
        key = 'test'
        value = StructureMock('test_value')
        subject = Map({key: value})
        map_overlay: Optional[MapOverlay] = MapOverlay(
            self.visitor,
            subject
        )
        get = map_overlay.value[key]
        self.assertEqual(get, value)
        self.assertEqual(self.visitor.structure, value)
        self.assertEqual(self.visitor.visit_structure_count, 1)

    def test_can_get_repr(self):
        representation: str = self.map_overlay.__repr__()
        self.assertTrue(representation.startswith('MapOverlay('))
