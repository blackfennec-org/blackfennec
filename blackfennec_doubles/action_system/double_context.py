from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.structure.double_structure import StructureMock


class ContextMock:
    def __init__(self, window=None):
        self.structure = StructureMock()
        self.window = window or Dummy('window')
