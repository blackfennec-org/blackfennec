from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from core import CORE_EXTENSION

class ToUpperAction(Action):
    def __init__(self):
        super().__init__(CORE_EXTENSION.types.string)

    def execute(self, context: Context):
        context.structure.value = context.structure.value.upper()
