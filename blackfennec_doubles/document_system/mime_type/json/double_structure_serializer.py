# -*- coding: utf-8 -*-

class StructureSerializerMock:
    def __init__(
            self,
            serialize_result=None,
            deserialize_result=None,
    ):
        self.serialize_count = 0
        self.serialize_parameter_structure = None
        self.serialize_result = serialize_result
        self.deserialize_count = 0
        self.deserialize_parameter_raw = None
        self.deserialize_result = deserialize_result

    def serialize(self, structure):
        self.serialize_count += 1
        self.serialize_parameter_structure = structure
        return self.serialize_result

    def deserialize(self, raw):
        self.deserialize_count += 1
        self.deserialize_parameter_raw = raw
        return self.deserialize_result
