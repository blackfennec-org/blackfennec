# -*- coding: utf-8 -*-
from io import StringIO

import pytest

from doubles.black_fennec.util.document.mime_type.types.double_structure_encoding_service import \
    StructureEncodingServiceMock
from doubles.black_fennec.util.document.mime_type.types.double_structure_parsing_service import \
    StructureParsingServiceMock
from doubles.double_dummy import Dummy
from src.black_fennec.util.document.mime_type.types.json.json_mime_type import JsonMimeType


@pytest.fixture()
def json_string():
    return '{"test": "test"}'


@pytest.fixture()
def raw_json():
    return {'test': 'test'}


@pytest.fixture()
def json_file(json_string):
    return StringIO(json_string)


@pytest.fixture()
def structure_encoder(json_string):
    return StructureEncodingServiceMock(encode_result=json_string)


@pytest.fixture()
def structure_decoder():
    return StructureParsingServiceMock()


@pytest.fixture()
def json_mime_type(structure_encoder, structure_decoder):
    return JsonMimeType(structure_encoder, structure_decoder)


def test_can_construct(json_mime_type):
    pass


def test_import_structure(json_mime_type, structure_decoder, json_file):
    json_mime_type.import_structure(json_file)

    assert structure_decoder.from_json_count == 1


def test_export_structure(json_mime_type, structure_encoder, json_string):
    structure_dummy = Dummy()
    tmp_json_file = StringIO()
    json_mime_type.export_structure(tmp_json_file, structure_dummy)
    assert structure_encoder.encode_count == 1

    tmp_json_file.seek(0)
    assert tmp_json_file.read() == json_string
