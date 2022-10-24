# -*- coding: utf-8 -*-
from blackfennec.document_system.mime_type.json.json_pointer_serializer import JsonPointerSerializer
from blackfennec.structure.reference_navigation.navigator import Navigator


class JsonPointerSerializerMock(JsonPointerSerializer):
    def __init__(
            self,
            serialize_result=None,
            deserialize_absolute_pointer_result=None,
            deserialize_relative_pointer_result=None,
    ):
        self.serialize_count = 0
        self.serialize_parameter_navigator = None
        self._serialize_result = serialize_result
        self.deserialize_absolute_pointer_count = 0
        self.deserialize_absolute_pointer_parameter_pointer = None
        self._deserialize_absolute_pointer_result = deserialize_absolute_pointer_result
        self.deserialize_relative_pointer_count = 0
        self.deserialize_relative_pointer_parameter_pointer = None
        self._deserialize_relative_pointer_result = deserialize_relative_pointer_result

    def serialize(self, navigator: Navigator):
        self.serialize_count += 1
        self.serialize_parameter_navigator = navigator
        return self._serialize_result

    def deserialize_absolute_pointer(self, pointer: str) -> Navigator:
        self.deserialize_absolute_pointer_count += 1
        self.deserialize_absolute_pointer_parameter_pointer = pointer
        return self._deserialize_absolute_pointer_result

    def deserialize_relative_pointer(self, pointer: str) -> Navigator:
        self.deserialize_relative_pointer_count += 1
        self.deserialize_relative_pointer_parameter_pointer = pointer
        return self._deserialize_relative_pointer_result
