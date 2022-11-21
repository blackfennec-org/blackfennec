import pytest

from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.type_system.boolean_type import BooleanType
from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.document_system.mime_type.json.json_pointer_serializer import (
    JsonPointerSerializer,
)
from blackfennec.document_system.mime_type.json.json_reference_serializer import (
    JsonReferenceSerializer,
)
from blackfennec.structure.structure_serializer import (
    StructureSerializer,
)
from blackfennec.document_system.mime_type.mime_type_registry import (
    MimeTypeRegistry,
)
from blackfennec.document_system.mime_type.json.json_mime_type import (
    JsonMimeType,
)
from blackfennec.document_system.resource_type.protocols.file_resource_type import (
    FileResourceType,
)
from blackfennec.document_system.resource_type.resource_type_registry import (
    ResourceTypeRegistry,
)
from blackfennec.type_system.type_loader import TypeLoader
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.null import Null
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.string import String
from blackfennec.type_system.type_registry import TypeRegistry
from blackfennec.document_system.resource_type.protocols.bftype_resource_type import BFTypeResourceType
from blackfennec.document_system.mime_type.in_memory.in_memory_mime_type import InMemoryMimeType
from blackfennec.layers.merge.merged_layer import MergedLayer

pytestmark = pytest.mark.integration


@pytest.fixture
def type_registry():
    return TypeRegistry()


@pytest.fixture
def document_factory(type_registry) -> DocumentFactory:
    resource_type_registry = ResourceTypeRegistry()
    resource_types = [
        FileResourceType(),
        BFTypeResourceType(type_registry),
    ]
    for resource_type in resource_types:
        for protocol in resource_type.protocols:
            resource_type_registry.register_resource_type(
                protocol, resource_type)

    mime_type_registry = MimeTypeRegistry()
    document_factory = DocumentFactory(
        DocumentRegistry(), resource_type_registry, mime_type_registry)
    reference_parser = JsonReferenceSerializer(
        document_factory, JsonPointerSerializer)
    structure_serializer = StructureSerializer(reference_parser)
    mime_types = [
        JsonMimeType(structure_serializer),
        InMemoryMimeType(),
    ]
    for mime_type in mime_types:
        mime_type_registry.register_mime_type(
            mime_type.mime_type_id, mime_type)
    return document_factory


@pytest.fixture
def type(tmp_path, document_factory, type_registry):
    divinetype_json = tmp_path / "divinetype.json"
    divinetype_json.write_text("""
{
    "super": {
        "super": null,
        "type": "Map"
    },
    "type": "DivineType",
    "properties": {
        "property0": {
            "super": null,
            "type": "Null"
        }
    }
}
""")

    supertype_json = tmp_path / "supertype.json"
    supertype_json.write_text("""
{
    "super": { "$ref": "bftype://DivineType"},
    "type": "SuperType",
    "required": [
        "property2",
        "property3"
    ],
    "properties": {
        "property1": {
            "super": null,
            "type": "String",
            "pattern": ".{3,}"
        },
        "property2": {
            "super": null,
            "type": "Number",
            "minimum": 0,
            "maximum": 100
        },
        "property3": {
            "super": {
                "super": null,
                "type": "Boolean"
            },
            "expected": true
        }
    }
}
""")

    subtype_json = tmp_path / "subtype.json"
    subtype_json.write_text("""
{
    "super": { "$ref": "bftype://SuperType" },
    "type": "SubType",
    "required": [
        "property1"
    ],
    "properties": {
        "property2": {
            "minimum": 10,
            "default": 1337
        }
    }
}
"""
                            )

    tl = TypeLoader(document_factory, type_registry)
    tl.load(divinetype_json.as_uri())
    tl.load(supertype_json.as_uri())
    return tl.load(subtype_json.as_uri())


def test_merges_recursively(type):
    assert "property0" in type.properties


def test_for_subclass_property(type):
    assert "property2" in type.properties


def test_for_superclass_property(type):
    assert "property1" in type.properties


def test_overrides_minimum(type):
    assert type.properties["property2"].minimum == 10


def test_inherits_maximum(type):
    assert type.properties["property2"].maximum == 100


def test_overrides_default(type):
    assert type.properties["property2"].default.value == 1337


def test_inheritance_in_inherited(type):
    assert isinstance(type.properties["property3"], BooleanType)


def test_overrides_nested_constraintes(type):
    assert type.properties["property3"].expected == True


def test_type_covers_good_instance(type):
    assert type.calculate_coverage(Map({
        "property1": String("abc"),
        "property2": Number(10),
        "property3": Boolean(True)
    })).is_covered()


@pytest.mark.parametrize(
    "merger",
    [lambda s: MergedLayer().apply(s, Null()),
        lambda s: MergedLayer().apply(Null(), s)],
    ids=["s_null", "null_s"],
)
@pytest.mark.parametrize(
    "structure",
    [Null(), Boolean(True), Number(1), String("a"), List(), Map()],
    ids=["null", "boolean", "number", "string", "list", "map"],
)
def test_merge_null(merger, structure):
    assert merger(structure).value == structure.value
