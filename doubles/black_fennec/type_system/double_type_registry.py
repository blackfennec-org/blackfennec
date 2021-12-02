from doubles.black_fennec.interpretation.auction.double_coverage import CoverageMock
from doubles.visualisation.double_structure_bidder import StructureBidderMock
from doubles.visualisation.double_structure_view_factory import StructureViewFactoryMock


class TypeRegistryMock:

    def __init__(self, types=None):
        if type is None:
            self._types = dict()
            self._types[StructureBidderMock(coverage=CoverageMock(1))] = StructureViewFactoryMock()
            self._types[StructureBidderMock(coverage=CoverageMock(2))] = StructureViewFactoryMock()
        self._types = types
        self.types_getter_count = 0

        self.register_type_count = 0
        self.register_type_last_bidder = None

        self.deregister_type_count = 0
        self.deregister_type_last_bidder = None


    @property
    def types(self):
        self.types_getter_count += 1
        return self._types

    def register_type(self, type_bidder):
        self.register_type_last_bidder = type_bidder
        self.register_type_count += 1

    def deregister_type(self, type_bidder):
        self.deregister_type_last_bidder = type_bidder
        self.deregister_type_count += 1
