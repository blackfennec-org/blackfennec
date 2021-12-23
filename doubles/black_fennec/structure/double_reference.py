from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.reference import Reference


class ReferenceMock(StructureMock):
    def __init__(self, value=None, parent=None, root=None, destination=None):
        StructureMock.__init__(self, value, parent, root)
        self.type_name = 'Reference'
        self._json_reference_resolve_service = None
        self._destination = destination
        self.get_destination_count = 0

    @property
    def destination(self):
        self.get_destination_count += 1
        return self._destination

    def accept(self, visitor):
        return visitor.visit_reference(self)


class ReferenceInstanceMock(ReferenceMock, Reference):
    def __init__(self, reference_resolving_service=None, reference=None):
        self.reference_resolving_service = reference_resolving_service\
            if reference_resolving_service\
            else JsonReferenceResolvingServiceMock()
        Reference.__init__(self, self.reference_resolving_service, reference)
        ReferenceMock.__init__(self, reference)
