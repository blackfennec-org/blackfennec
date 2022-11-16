from blackfennec_doubles.structure.double_structure import StructureMock

class HistoryEntryMock:
    def __init__(self, structure=None, old=None, new=None) -> None:
        self.structure = structure or StructureMock()
        self.old = old
        self.new = new