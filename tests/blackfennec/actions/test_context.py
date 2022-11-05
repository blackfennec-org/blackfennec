from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.actions.context import Context

def test_can_get_structure():
    structure = StructureMock()
    context = Context(structure)
    assert context.structure == structure