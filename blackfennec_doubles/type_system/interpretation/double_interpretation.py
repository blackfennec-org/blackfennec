from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.presentation_system.double_structure_view import StructureViewDummy
from blackfennec.type_system.interpretation.specification import Specification

class InterpretationMock:
    def __init__(self, 
            structure=None, 
            structure_view=None, 
            specification=None,
            types=None):
        self.navigation_requests = list()
        self.structure_property_access_count = 0
        self._structure = structure or StructureMock()
        self.structure_view = structure_view or StructureViewDummy()
        self.navigation_service = None
        self.specification = specification or Specification()
        self.types = types or []

    def set_navigation_service(self, navigation_service):
        self.navigation_service = navigation_service

    def navigate(self, structure):
        self.navigation_requests.append(structure)

    @property
    def structure(self):
        self.structure_property_access_count += 1
        return self._structure
