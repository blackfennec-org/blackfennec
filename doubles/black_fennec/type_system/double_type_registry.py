from doubles.black_fennec.interpretation.auction.double_coverage import CoverageMock
from doubles.black_fennec.structure.type.double_type import TypeMock


class TypeRegistryMock:
    def __init__(self, types=None):
        if type is None:
            self._types = [
                TypeMock("Type1", CoverageMock(1)),
                TypeMock("Type2", CoverageMock(2)),
            ]
        self._types = types
        self.types_getter_count = 0

        self.register_type_count = 0
        self.register_type_last_type = None

        self.deregister_type_count = 0
        self.deregister_type_last_type = None

    @property
    def types(self):
        self.types_getter_count += 1
        return self._types

    def register_type(self, type):
        self.register_type_last_type = type
        self.register_type_count += 1

    def deregister_type(self, type):
        self.deregister_type_last_type = type
        self.deregister_type_count += 1
