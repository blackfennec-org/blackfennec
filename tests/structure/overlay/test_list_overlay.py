import unittest
from typing import Optional

from doubles.structure.double_info import InfoMock
from doubles.structure.overlay.double_overlay_factory import OverlayFactoryMock
from doubles.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.info import Info
from src.structure.list import List
from src.structure.reference import Reference
from src.structure.root import Root
from src.structure.overlay.list_overlay import ListOverlay
from src.structure.overlay.overlay_factory import _get_overlay_class


class ListOverlayTestSuite(unittest.TestCase):
    def setUp(self):
        self.factory = OverlayFactoryMock()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_overlay: Optional[ListOverlay] = ListOverlay(self.subject, self.factory)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.list_overlay: Optional[ListOverlay] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.list_overlay.subject, self.subject)

    def test_get_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_overlay: Optional[ListOverlay] = ListOverlay(
            subject,
            self.factory
        )
        get = list_overlay[0]
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_set_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_overlay: Optional[ListOverlay] = ListOverlay(
            subject,
            self.factory
        )
        new_value = InfoMock('new_value')
        list_overlay[0] = new_value
        self.assertNotIn(value, list_overlay.subject)
        self.assertIn(new_value, list_overlay.subject)

    def test_append_item(self):
        value = InfoMock('test_value')
        self.factory._create_return = value
        self.list_overlay.append(value)
        self.assertIn(value, self.list_overlay.children)

    def test_append_item_already_encapsulated(self):
        value = InfoMock('test_value')
        overlay_class = _get_overlay_class(Info)
        encapsulated = overlay_class(value, self.factory)
        self.factory._create_return = encapsulated
        self.list_overlay.append(encapsulated)
        self.assertIn(value, self.list_overlay.subject.children)

    def test_get_children(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_overlay: Optional[ListOverlay] = ListOverlay(
            subject,
            self.factory
        )
        children = list_overlay.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_children_with_reference(self):
        value = InfoMock('test_value')
        resolving_service = JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, '0')
        subject = List([ref])
        self.factory._create_return = value
        list_overlay: Optional[ListOverlay] = ListOverlay(
            subject,
            self.factory
        )
        children = list_overlay.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_empty_children(self):
        children = self.list_overlay.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.factory._create_calls, 0)

    def test_remove_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_overlay: Optional[ListOverlay] = ListOverlay(
            subject,
            self.factory
        )
        list_overlay.remove(value)
        self.assertEqual(len(self.subject), 0)

    def test_remove_encapsulated_item(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        list_overlay: Optional[ListOverlay] = ListOverlay(
            subject,
            self.factory
        )
        overlay_class = _get_overlay_class(Info)
        encapsulated = overlay_class(value, self.factory)
        list_overlay.remove(encapsulated)
        self.assertEqual(len(self.subject), 0)

    def test_remove_item_not_in_list(self):
        value = InfoMock('test_value')
        subject = List([value])
        self.factory._create_return = value
        with self.assertRaises(KeyError):
            self.list_overlay.remove(value)

    def test_can_get_repr(self):
        representation: str = self.list_overlay.__repr__()
        self.assertTrue(representation.startswith('ListOverlay('))
