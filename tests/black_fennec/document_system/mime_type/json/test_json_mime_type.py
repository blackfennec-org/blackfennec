# -*- coding: utf-8 -*-
from io import StringIO

import pytest

from doubles.black_fennec.document_system.mime_type.json.double_structure_serializer import \
    StructureSerializerMock
from doubles.double_dummy import Dummy
from src.black_fennec.document_system.mime_type.json.json_mime_type import JsonMimeType


@pytest.fixture()
def json_string():
    return '''{
  "test": "test"
}'''


@pytest.fixture()
def raw_json():
    return {'test': 'test'}


@pytest.fixture()
def json_file(json_string):
    return StringIO(json_string)


@pytest.fixture()
def structure_serializer(raw_json):
    return StructureSerializerMock(serialize_result=raw_json)


@pytest.fixture()
def json_mime_type(structure_serializer):
    return JsonMimeType(structure_serializer)


def test_can_construct(json_mime_type):
    pass


def test_import_structure(json_mime_type, structure_serializer, json_file):
    json_mime_type.import_structure(json_file)
    assert structure_serializer.deserialize_count == 1


def test_export_structure(json_mime_type, structure_serializer, json_string):
    structure_dummy = Dummy()
    tmp_json_file = StringIO()
    json_mime_type.export_structure(tmp_json_file, structure_dummy)
    assert structure_serializer.serialize_count == 1

    tmp_json_file.seek(0)
    assert tmp_json_file.read() == json_string
