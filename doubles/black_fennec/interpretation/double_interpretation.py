from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.visualisation.double_structure_view import StructureViewDummy


class InterpretationMock:
    def __init__(self, structure = None, structure_view = None):
        self.navigation_requests = list()
        self.view_property_access_count = 0
        self.structure_property_access_count = 0
        self._structure = StructureMock() if structure is None else structure
        self.structure_view = StructureViewDummy() if structure_view is None else structure_view
        self.navigation_service = None

    def set_navigation_service(self, navigation_service):
        self.navigation_service = navigation_service

    def navigate(self, structure):
        self.navigation_requests.append(structure)

    @property
    def view(self):
        self.view_property_access_count += 1
        return self.structure_view

    @property
    def structure(self):
        self.structure_property_access_count += 1
        return self._structure
