import pytest

from blackfennec_doubles.type_system import TypeMock
from blackfennec.action_system import Action

class ConcreteAction(Action):
    def __init__(self, type=None):
        super().__init__(type or TypeMock())
    def execute(self, context):
        pass
    @property
    def name(self):
        return "name"
    @property
    def description(self):
        return "description"

def test_can_construct_action():
    action = ConcreteAction()
    assert action is not None

def test_must_override_execute():
    class ConcreteAction(Action):
        def __init__(self):
            super().__init__(TypeMock())
        
    with pytest.raises(TypeError):
        ConcreteAction()

def test_can_get_type():
    type = TypeMock()
    action = ConcreteAction(type)
    assert action.type == type

def test_can_execute():
    """Ensure the interface of the execute function is correct"""    
    action = ConcreteAction()
    action.execute(None)