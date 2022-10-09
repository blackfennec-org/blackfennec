import json

import pytest

from doubles.black_fennec.document_system.mime_type.json.double_json_reference_serializer import \
    JsonReferenceSerializerMock
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.structure.null import Null
from tests.test_utils.deep_compare import DeepCompare
from src.black_fennec.structure.structure_serializer import StructureSerializer


@pytest.fixture()
def json_reference_serializer():
    return JsonReferenceSerializerMock(deserialize_result=[])


@pytest.fixture()
def structure_serializer(json_reference_serializer):
    return StructureSerializer(json_reference_serializer)


def test_can_construct():
    pass


@pytest.mark.parametrize('structure, expected', [
    (List(), []),
    (Map(), {}),
    (String(''), ''),
    (String('0'), '0'),
    (String('Black Fennec'), 'Black Fennec'),
    (Number(0), 0),
    (Number(1337), 1337),
    (Number(3.141), 3.141),
    (Boolean(True), True),
    (Boolean(False), False),
    (Null(), None),
    (Reference([]), {"$ref": None}),
    (
            Map({
                'key': String('value'),
                'null': Null()
            }),
            {
                'key': 'value',
                'null': None
            }
    ),
    (
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
            }),
            {
                'Tim': {
                    'firstname': 'Timo',
                    'lastname': 'Turbo',
                    'age': 42,
                    'hobbies': ['climbing', 'soccer']
                }
            }
    ),
    (
            Map({
                'continents': List([
                    Map({'identification': String('Asia'), 'countries':
                        List([String('Russia'), String('China')])}),
                    Map({'identification': String('Africa'), 'countries':
                        List([String('Nigeria'), String('Ethiopia')])}),
                ])
            }),
            {
                'continents': [
                    {'identification': 'Asia', 'countries':
                        ['Russia', 'China']},
                    {'identification': 'Africa', 'countries':
                        ['Nigeria', 'Ethiopia']},
                ]
            }
    )
])
def test_serialize(structure, expected, structure_serializer):
    result = structure_serializer.serialize(structure)
    result_string = json.dumps(result)
    expected_string = json.dumps(expected)
    assert result_string == expected_string


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
    ({"$ref": ""}, Reference([])),
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
def test_deserialize(raw, expected, structure_serializer):
    result = structure_serializer.deserialize(raw)
    assert DeepCompare.compare(result, expected)


def test_throws_error_on_serialization_of_unknown_type(structure_serializer):
    o = object()

    with pytest.raises(NotImplementedError):
        structure_serializer.serialize(o)


def test_throws_error_on_deserialization_of_unknown_type(structure_serializer):
    o = object()

    with pytest.raises(NotImplementedError):
        structure_serializer.deserialize(o)
