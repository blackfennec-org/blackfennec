class MessageMock:
    def __init__(self, text, action_name=None, action_target=None):
        self.text = text
        self.action_name = action_name
        self.action_target = action_target
