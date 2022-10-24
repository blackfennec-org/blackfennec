# -*- coding: utf-8 -*-
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.structure.reference import Reference


class ReferenceMock(StructureMock):
    def __init__(self, value=None, parent=None, root=None, resolve_return=None):
        StructureMock.__init__(self, value, parent, root)
        self.type_name = 'Reference'
        self._json_reference_resolve_service = None
        self._resolve_return = resolve_return
        self.resolve_count = 0

    def resolve(self):
        self.resolve_count += 1
        return self._resolve_return

    def accept(self, visitor):
        return visitor.visit_reference(self)


class ReferenceInstanceMock(Reference, ReferenceMock):
    def __init__(self, reference=None):
        reference = reference or []
        Reference.__init__(self, reference)
        ReferenceMock.__init__(self, reference)
