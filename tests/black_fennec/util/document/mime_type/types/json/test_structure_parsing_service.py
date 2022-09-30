import pytest

from doubles.black_fennec.util.document.mime_type.types.double_json_reference_parser import JsonReferenceParserMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.structure.null import Null
from tests.test_utils.deep_compare import DeepCompare
from src.black_fennec.util.document.mime_type.types.json.structure_parsing_service import StructureParsingService


@pytest.fixture()
def json_reference_parser():
    return JsonReferenceParserMock()


@pytest.fixture()
def structure_decoder(json_reference_parser):
    return StructureParsingService(json_reference_parser)


def test_can_construct():
    pass


@pytest.mark.parametrize('raw, expected', [
    ([], List()),
    ({}, Map()),
    ('', String('')),
    ('0', String('0')),
    ('Black Fennec', String('Black Fennec')),
    (0, Number(0)),
    (1337, Number(1337)),
    (3.141, Number(3.141)),
    (True, Boolean(True)),
    (False, Boolean(False)),
    (None, Null()),
    (
            {
                'key': 'value',
                'null': None
            },
            Map({
                'key': String('value'),
                'null': Null()
            })
    ),
    (
            {
                'Tim': {
                    'firstname': 'Timo',
                    'lastname': 'Turbo',
                    'age': 42,
                    'hobbies': ['climbing', 'soccer']
                }
            },
            Map({
                'Tim': Map({
                    'firstname': String('Timo'),
                    'lastname': String('Turbo'),
                    'age': Number(42),
                    'hobbies': List([
                        String('climbing'),
                        String('soccer')
                    ])
                })
            })
    ),
    (
            {
                'continents': [
                    {'identification': 'Asia', 'countries':
                        ['Russia', 'China']},
                    {'identification': 'Africa', 'countries':
                        ['Nigeria', 'Ethiopia']},
                ]
            },
            Map({
                'continents': List([
                    Map({'identification': String('Asia'), 'countries':
                        List([String('Russia'), String('China')])}),
                    Map({'identification': String('Africa'), 'countries':
                        List([String('Nigeria'), String('Ethiopia')])}),
                ])
            })
    )
])
def test_parse(raw, expected, structure_decoder):
    result = structure_decoder.from_json(raw)
    assert DeepCompare.compare(result, expected)


def test_throws_error_on_unknown_type(structure_decoder):
    o = object()

    with pytest.raises(TypeError):
        structure_decoder.from_json(o)


def test_can_parse_json_reference_to_reference(structure_decoder):
    data = {'$ref': 'ref'}
    result: Reference = structure_decoder.from_json(data)
    assert isinstance(result, Reference)
