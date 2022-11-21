

from blackfennec_doubles.structure.double_structure import StructureMock


class MergedLayerMock:
    def __init__(self, returns=None):
        self.returns = returns or StructureMock()

    def apply(self, underlay, overlay):
        return self.returns