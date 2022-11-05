from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from core import CORE_EXTENSION

class ToLowerAction(Action):
    def __init__(self):
        super().__init__(CORE_EXTENSION.types.string)

    def execute(self, context: Context):
        context.structure.value = context.structure.value.lower()

    @property
    def name(self):
        return "to lower"

    @property
    def description(self):
        return """Converts the string to lower case."""
