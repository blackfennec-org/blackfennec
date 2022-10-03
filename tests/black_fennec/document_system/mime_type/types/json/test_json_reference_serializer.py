import pytest

from doubles.black_fennec.document_system.double_document import DocumentMock
from doubles.black_fennec.document_system.double_document_factory import DocumentFactoryMock
from doubles.black_fennec.document_system.mime_type.types.double_json_pointer_parser import JsonPointerSerializerMock
from src.black_fennec.document_system.mime_type.types.json.json_reference_serializer import JsonReferenceSerializer
from src.black_fennec.structure.map import Map
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
    return JsonReferenceSerializer(document_factory, JsonPointerSerializerMock())


def test_can_construct(json_reference_parser):
    pass


@pytest.mark.parametrize("reference, expected", [
    ({JsonReferenceSerializer.REFERENCE_KEY: 'https://test.test/test.json'}, [
        UriNavigator(pytest.lazy_fixture("document_factory"), 'https://test.test/test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY: 'C:/test.json'}, [
        UriNavigator(pytest.lazy_fixture("document_factory"), 'C:/test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY: './test.json'}, [
        UriNavigator(pytest.lazy_fixture("document_factory"), './test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY: 'test.json'}, [
        UriNavigator(pytest.lazy_fixture("document_factory"), 'test.json')
    ]),
    ({JsonReferenceSerializer.REFERENCE_KEY + "_make_invalid": "test"}, KeyError)
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
