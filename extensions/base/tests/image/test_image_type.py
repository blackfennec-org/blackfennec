import pytest
from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.document_system.mime_type.mime_type_registry import (
    MimeTypeRegistry,
)
from blackfennec.document_system.mime_type.in_memory.in_memory_mime_type import (
    InMemoryMimeType,
)
from blackfennec.document_system.mime_type.json.json_mime_type import (
    JsonMimeType,
)
from blackfennec.document_system.mime_type.json.json_pointer_serializer import (
    JsonPointerSerializer,
)
from blackfennec.document_system.mime_type.json.json_reference_serializer import (
    JsonReferenceSerializer,
)
from blackfennec.structure.structure_serializer import (
    StructureSerializer,
)
from blackfennec.document_system.resource_type.protocols.bftype_resource_type import (
    BFTypeResourceType,
)
from blackfennec.document_system.resource_type.protocols.file_resource_type import (
    FileResourceType,
)
from blackfennec.document_system.resource_type.resource_type_registry import (
    ResourceTypeRegistry,
)
from blackfennec.structure.type.boolean_type import BooleanType
from blackfennec.structure.type.list_type import ListType
from blackfennec.structure.type.map_type import MapType
from blackfennec.structure.type.null_type import NullType
from blackfennec.structure.type.number_type import NumberType
from blackfennec.structure.type.string_type import StringType
from blackfennec.structure.type.type_loader import TypeLoader
from blackfennec.structure.string import String
from blackfennec.structure.map import Map
from blackfennec.type_system.type_registry import TypeRegistry


@pytest.fixture
def type_registry():
    type_registry = TypeRegistry()
    type_registry.register_type(MapType())
    type_registry.register_type(ListType())
    type_registry.register_type(StringType())
    type_registry.register_type(NumberType())
    type_registry.register_type(BooleanType())
    type_registry.register_type(NullType())

    return type_registry


@pytest.fixture
def document_factory(type_registry) -> DocumentFactory:
    resource_type_registry = ResourceTypeRegistry()
    resource_types = [
        FileResourceType(),
        BFTypeResourceType(type_registry),
    ]
    for resource_type in resource_types:
        for protocol in resource_type.protocols:
            resource_type_registry.register_resource_type(protocol, resource_type)

    mime_type_registry = MimeTypeRegistry()
    document_factory = DocumentFactory(resource_type_registry, mime_type_registry)
    reference_parser = JsonReferenceSerializer(document_factory, JsonPointerSerializer)
    structure_serializer = StructureSerializer(reference_parser)
    mime_types = [
        JsonMimeType(structure_serializer),
        InMemoryMimeType(),
    ]
    for mime_type in mime_types:
        mime_type_registry.register_mime_type(mime_type.mime_type_id, mime_type)
    return document_factory


@pytest.fixture
def type_loader(document_factory, type_registry):
    return TypeLoader(document_factory, type_registry)


@pytest.fixture
def type(type_loader):
    type_loader.load("base/file/file.json")
    return type_loader.load("base/image/image.json")


def test_can_load(type):
    assert type is not None


def test_name_is_image(type):
    assert type.name == "Image"


def test_super_type_is_file(type):
    assert type.super.name == "File"


def test_can_access_file_path(type):
    assert isinstance(type.properties["file_path"], StringType)


def test_file_path_is_required(type):
    assert not type.properties["file_path"].is_optional


def test_can_cover_image(type):
    assert type.calculate_coverage(
        Map(
            {"file_path": String("examples/logo.jpg"), "file_type": String("image/jpg")}
        )
    ).is_covered()
