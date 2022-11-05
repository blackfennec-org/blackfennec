import pytest

from blackfennec_doubles.type_system import TypeMock
from blackfennec.actions import Action

def test_can_construct_action():
    class ConcreteAction(Action):
        def __init__(self):
            super().__init__(TypeMock())
        def execute(self, context):
            pass
        
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
    class ConcreteAction(Action):
        def __init__(self):
            super().__init__(type)
        def execute(self, context):
            pass
        
    action = ConcreteAction()
    assert action.type == type

def test_can_execute():
    """ Ensure the interface of the execute function is correct """
    class ConcreteAction(Action):
        def __init__(self):
            super().__init__(TypeMock())
        def execute(self, context):
            pass
        
    action = ConcreteAction()
    action.execute(None)