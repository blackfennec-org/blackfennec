from blackfennec.structure.structure import Structure


class Context:
    """Context is the context in which an action is called.

    Attributes:
        structure (Structure): the structure on which the action is called
    """

    def __init__(self, structure: Structure):
        self.structure = structure
