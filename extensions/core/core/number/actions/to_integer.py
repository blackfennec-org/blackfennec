from decimal import Decimal

from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from core import CORE_EXTENSION


class ToIntegerAction(Action):
    def __init__(self):
        super().__init__(CORE_EXTENSION.types.number)

    def execute(self, context: Context):
        context.structure.value = int(context.structure.value)

    @property
    def name(self):
        return "to integer"

    @property
    def description(self):
        return """Converts the number to integer."""
