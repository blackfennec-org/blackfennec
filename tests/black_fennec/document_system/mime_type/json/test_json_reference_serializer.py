import pytest
from pytest_lazyfixture import lazy_fixture

from doubles.black_fennec.document_system.double_document import DocumentMock
from doubles.black_fennec.document_system.double_document_factory import DocumentFactoryMock
from doubles.black_fennec.document_system.mime_type.json.double_json_pointer_parser import \
    JsonPointerSerializerMock
from src.black_fennec.document_system.mime_type.json.json_reference_serializer import JsonReferenceSerializer
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.reference_navigation.root_navigator import RootNavigator
from src.black_fennec.structure.reference_navigation.uri_navigator import UriNavigator
from src.black_fennec.structure.root_factory import RootFactory
from src.black_fennec.structure.string import String


@pytest.fixture()
def document():
    data = {
        'key': String('value')
    }
    structure_map = Map(data)
    document = DocumentMock(content=structure_map)
    RootFactory.make_root(structure_map, document)
    return document


@pytest.fixture()
def document_factory(document):
    return DocumentFactoryMock(create_return=document)


@pytest.fixture()
def json_reference_parser(document_factory):
    return JsonReferenceSerializer(
        document_factory,
        JsonPointerSerializerMock(
            serialize_result='pointer',
            deserialize_relative_pointer_result=[],
            deserialize_absolute_pointer_result=[RootNavigator()]
        )
    )


def test_can_construct(json_reference_parser):
    pass


@pytest.mark.parametrize("reference, expected", [
    (
            [UriNavigator(lazy_fixture("document_factory"), 'https://test.test/test.json')],
            {JsonReferenceSerializer.REFERENCE_KEY: 'https://test.test/test.json'}
    ),
    (
            [UriNavigator(lazy_fixture("document_factory"), 'C:/test.json')],
            {JsonReferenceSerializer.REFERENCE_KEY: 'C:/test.json'}
    ),
    (
            [UriNavigator(lazy_fixture("document_factory"), './test.json')],
            {JsonReferenceSerializer.REFERENCE_KEY: './test.json'}
    ),
    (
            [UriNavigator(lazy_fixture("document_factory"), 'test.json')],
            {JsonReferenceSerializer.REFERENCE_KEY: 'test.json'}
    ),
    (
            [RootNavigator()],
            {JsonReferenceSerializer.REFERENCE_KEY: '#/pointer'}
    ),
    (
            [],
            {JsonReferenceSerializer.REFERENCE_KEY: None}
    )
])
def test_serialize_json_reference(json_reference_parser, reference, expected):
    relative_pointer = json_reference_parser.serialize(reference)
    assert relative_pointer == expected


@pytest.mark.parametrize("reference, expected", [
    ({JsonReferenceSerializer.REFERENCE_KEY: 'https://test.test/test.json'}, [
        UriNavigator(lazy_fixture("document_factory"), 'https://test.test/test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY: 'C:/test.json'}, [
        UriNavigator(lazy_fixture("document_factory"), 'C:/test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY: './test.json'}, [
        UriNavigator(lazy_fixture("document_factory"), './test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY: 'test.json'}, [
        UriNavigator(lazy_fixture("document_factory"), 'test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY + "_make_invalid": "test"}, KeyError),
    ({JsonReferenceSerializer.REFERENCE_KEY: None}, []),
    ({JsonReferenceSerializer.REFERENCE_KEY: '#0-1/key'}, []),
    ({JsonReferenceSerializer.REFERENCE_KEY: '#key/1'}, [RootNavigator()]),
])
def test_parse_json_reference(json_reference_parser, reference, expected):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(expected):
            json_reference_parser.deserialize(reference)
            return
    else:
        relative_pointer = json_reference_parser.deserialize(reference)
        assert relative_pointer == expected


def test_is_json_reference():
    reference = dict()
    reference[JsonReferenceSerializer.REFERENCE_KEY] = 'ref'
    assert JsonReferenceSerializer.is_reference(reference)


def test_is_json_reference_with_no_json_reference():
    reference = dict()
    reference[JsonReferenceSerializer.REFERENCE_KEY + '_make_invalid'] = 'ref'
    assert not JsonReferenceSerializer.is_reference(reference)
