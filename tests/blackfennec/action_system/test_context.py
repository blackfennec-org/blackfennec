from blackfennec_doubles.action_system.double_ui_context import UiContextMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.action_system.context import Context


def test_can_get_structure():
    structure = StructureMock()
    ui_context = UiContextMock(root=Dummy('window'))
    context = Context(ui_context, structure)
    assert context.structure == structure
    assert context.ui_context == ui_context
