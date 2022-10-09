import json
import pytest

from doubles.black_fennec.document_system.mime_type.types.json.double_json_reference_serializer import JsonReferenceSerializerMock
from src.black_fennec.document_system.mime_type.types.json.structure_serializer import StructureSerializer
from src.black_fennec.structure.merge.deep_merge import DeepMerge


@pytest.fixture
def parser():
    structure_serializer = StructureSerializer(JsonReferenceSerializerMock())
    return structure_serializer.deserialize
    

def test_merges_properites(parser):
    j = json.loads("""
{
    "super": {
        "a": {
            "b": "super.a.b"
        }
    },
    "a": {
        "c": "a.c"
    }
}
""")
    structure = parser(j)
    merged = DeepMerge.merge(structure.value["super"], structure)

    assert merged.value["a"].value["b"].value == "super.a.b"


@pytest.fixture
def structure(parser):
    j = json.loads("""
    {
        "super": {
            "super": {
                "super": null,
                "a": {
                    "a": "super.super.a.a"
                }
            },
            "b": {
                "b": "super.b.b"
            }
        },
        "c": {
            "c": "c.c"
        }
    }
    """)
    return parser(j)



def _merge_super(structure):
    super = structure.value["super"]
    if super.value is None:
        return structure
    merged_super = _merge_super(super)
    return DeepMerge.merge(underlay=merged_super, overlay=structure)

@pytest.fixture
def merged(structure):
    return _merge_super(structure)
    

def test_can_access_super_super(merged):
    assert merged.value["a"].value["a"].value == "super.super.a.a"

def test_can_access_super(merged):
    assert merged.value["b"].value["b"].value == "super.b.b"

def test_can_merge_merged_structure(merged):
    assert merged.value["c"].value["c"].value == "c.c"

def test_1(parser):
    j = json.loads("""
{
    "super": {
        "super": {
            "super": null
        },
        "b": {
            "value": "super.b.value"
        }
    }
}
""")
    s = parser(j)
    merged = _merge_super(s)
    b = merged.value["b"]
    assert b.value["value"].value == "super.b.value"

def test_2(parser):
    j = json.loads("""
{
    "super": {
        "super": {
            "super": null,
            "a": {
                "value": "super.a.value"
            }
        }
    }
}
""")
    s = parser(j)
    merged = _merge_super(s)
    a = merged.value["a"]
    assert a.value["value"].value == "super.a.value"