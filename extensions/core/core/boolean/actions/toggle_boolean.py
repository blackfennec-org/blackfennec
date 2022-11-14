from decimal import Decimal

from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from core import CORE_EXTENSION


class ToggleBooleanAction(Action):
    def __init__(self):
        super().__init__(CORE_EXTENSION.types.boolean)

    def execute(self, context: Context):
        context.structure.value = not context.structure.value

    @property
    def name(self):
        return "toggle"

    @property
    def description(self):
        return """Toggles the boolean."""
