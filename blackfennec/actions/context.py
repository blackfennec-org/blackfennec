from blackfennec.structure.structure import Structure


class Context:
    """Context is the context in which an action is called.

    Attributes:
        structure (Structure): the structure on which the action is called
    """

    def __init__(self, structure: Structure, ui_context):
        self.structure = structure
        self.ui_context = ui_context
        self.window = ui_context.get_root()
