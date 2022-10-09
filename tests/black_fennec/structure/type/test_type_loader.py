import pytest

from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.merge.deep_merge import DeepMerge
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.black_fennec.document_system.document_factory import DocumentFactory
from src.black_fennec.document_system.mime_type.types.json.json_pointer_serializer import (
    JsonPointerSerializer,
)
from src.black_fennec.document_system.mime_type.types.json.json_reference_serializer import (
    JsonReferenceSerializer,
)
from src.black_fennec.document_system.mime_type.types.json.structure_serializer import (
    StructureSerializer,
)
from src.black_fennec.document_system.mime_type.mime_type_registry import (
    MimeTypeRegistry,
)
from src.black_fennec.document_system.mime_type.types.json.json_mime_type import (
    JsonMimeType,
)
from src.black_fennec.document_system.resource_type.protocols.file_resource_type import (
    FileResourceType,
)
from src.black_fennec.document_system.resource_type.resource_type_registry import (
    ResourceTypeRegistry,
)
from src.black_fennec.structure.overlay.overlay_factory_visitor import (
    OverlayFactoryVisitor,
)
from src.black_fennec.structure.type.type_parser import TypeParser
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock

@pytest.fixture
def document_factory() -> DocumentFactory:
    resource_type_registry = ResourceTypeRegistry()
    resource_type = FileResourceType()
    for protocol in resource_type.protocols:
        resource_type_registry.register_resource_type(protocol, resource_type)

    mime_type_registry = MimeTypeRegistry()
    document_factory = DocumentFactory(resource_type_registry, mime_type_registry)
    reference_parser = JsonReferenceSerializer(document_factory, JsonPointerSerializer)
    structure_serializer = StructureSerializer(reference_parser)
    mime_type = JsonMimeType(structure_serializer)
    mime_type_registry.register_mime_type(mime_type.mime_type_id, mime_type)
    return document_factory


@pytest.fixture
def type_registry():
    return TypeRegistryMock()

@pytest.fixture
def type(tmp_path, document_factory, type_registry):
    type_json = tmp_path / "type.json"
    type_json.write_text(
        """
{
    "super": {
        "super": {
            "super": {
                "super": null,
                "type": "Map"
            },
            "type": "DevineType",
            "properties": {
                "property0": {
                    "super": null,
                    "type": "Null"
                }
            }
        },
        "type": "SuperType",
        "required": [],
        "properties": {
            "property1": {
                "super": null,
                "type": "String",
                "pattern": ".{3,}"
            },
            "property2": {
                "super": null,
                "type": "Number",
                "minimum": 0
            },
            "property3": {
                "super": {
                    "super": null,
                    "type": "Boolean"
                },
                "expected": true
            }
        }
    },
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
    return tl.load(type_json.as_uri())

class TypeLoader:
    def __init__(self, document_factory, type_registry):
        self._document_factory = document_factory
        self._visitors = [OverlayFactoryVisitor()]
        self._type_registry = type_registry

    def _apply_layers(self, structure):
        for visitor in self._visitors:
            structure = structure.accept(visitor)
        return structure
    
    def load(self, uri):
        document = self._document_factory.create(uri)
        structure = self._apply_layers(document.content)
        type = TypeParser.parse(structure)
        self._type_registry.register_type(type)
        return type


def test_merges_recursively(type):
    assert "property0" in type.properties


def test_for_subclass_property(type):
    assert "property2" in type.properties


def test_for_superclass_property(type):
    assert "property1" in type.properties


def test_overrides_minimum(type):
    assert type.properties["property2"].minimum == 10


def test_overrides_default(type):
    assert type.properties["property2"].default.value == 1337


def test_inheritance_in_inherited(type):
    assert isinstance(type.properties["property3"], BooleanType)


def test_overrides_nested_constraintes(type):
    assert type.properties["property3"].expected == True


@pytest.mark.parametrize(
    "merger",
    [lambda s: DeepMerge.merge(s, Null()), lambda s: DeepMerge.merge(Null(), s)],
    ids=["s_null", "null_s"],
)
@pytest.mark.parametrize(
    "structure",
    [Null(), Boolean(True), Number(1), String("a"), List(), Map()],
    ids=["null", "boolean", "number", "string", "list", "map"],
)
def test_merge_null(merger, structure):
    assert merger(structure).value == structure.value
