from decimal import Decimal

from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from core import CORE_EXTENSION


class DeleteMapItemsAction(Action):
    def __init__(self):
        super().__init__(CORE_EXTENSION.types.map)

    def execute(self, context: Context):
        context.structure.value = {}

    @property
    def name(self):
        return "delete items"

    @property
    def description(self):
        return """Deletes all items of the Dictionary."""
