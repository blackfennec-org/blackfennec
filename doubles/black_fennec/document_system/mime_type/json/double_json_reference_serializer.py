# -*- coding: utf-8 -*-


class JsonReferenceSerializerMock:
    REFERENCE_KEY = "$ref"

    def __init__(
            self,
            serialize_result=None,
            deserialize_result=None
    ):
        self.serialize_count = 0
        self.serialize_parameter_structure = None
        self._serialize_result = serialize_result
        self.deserialize_count = 0
        self.deserialize_parameter_raw = None
        self._deserialize_result = deserialize_result

    def serialize(self, structure):
        self.serialize_count += 1
        self.serialize_parameter_structure = structure
        return self._serialize_result

    def deserialize(self, raw):
        self.deserialize_count += 1
        self.deserialize_parameter_raw = raw
        return self._deserialize_result

    @classmethod
    def is_reference(cls, raw: dict):
        if cls.REFERENCE_KEY in raw.keys() and len(raw.keys()) == 1:
            return True
        else:
            return False
