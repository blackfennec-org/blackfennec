from doubles.structure.double_info import InfoMock
from doubles.util.file.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.reference import Reference


class ReferenceMock(InfoMock):
    def __init__(self, reference=None, destination=None):
        InfoMock.__init__(self)
        self._reference = reference
        self._destination = destination
        self.get_reference_count = 0
        self.set_reference_count = 0

    @property
    def reference(self):
        self.get_reference_count += 1
        return self._reference

    @reference.setter
    def reference(self, value: str):
        self.set_reference_count += 1
        self._reference = value

    @property
    def destination(self):
        return self._destination


class ReferenceInstanceMock(ReferenceMock, Reference):
    def __init__(self, reference_resolving_service=None, reference=None):
        self.reference_resolving_service = reference_resolving_service\
            if reference_resolving_service\
            else JsonReferenceResolvingServiceMock()
        Reference.__init__(self, self.reference_resolving_service, reference)
        ReferenceMock.__init__(self, reference)