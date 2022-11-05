
class ActionRegistryMock:
    def __init__(self):
        self.register_action_count = 0
        self.deregister_action_count = 0

    def register_action(self, action):
        self.register_action_count += 1

    def deregister_action(self, action):
        self.deregister_action_count += 1
