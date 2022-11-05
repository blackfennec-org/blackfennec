
class ActionMock:
    def __init__(self, type=None):
        self.type = type

        self.execute_count = 0
        self.execute_last_context = None

    def execute(self, context):
        self.execute_last_context = context
        self.execute_count += 1