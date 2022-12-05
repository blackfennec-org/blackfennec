from blackfennec_doubles.actions.double_ui_context import UiContextMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.actions.context import Context


def test_can_get_structure():
    structure = StructureMock()
    ui_context = UiContextMock(root=Dummy('window'))
    context = Context(structure, ui_context)
    assert context.structure == structure
