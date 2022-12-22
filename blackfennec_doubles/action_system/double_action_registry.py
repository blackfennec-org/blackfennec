class ActionRegistryMock:
    def __init__(self, actions=None):
        self.actions: dict = actions
        self.get_action_count = 0
        self.register_action_count = 0
        self.deregister_action_count = 0

    def get_actions(self, type):
        return self.actions[type]

    def register_action(self, action):
        self.register_action_count += 1

    def deregister_action(self, action):
        self.deregister_action_count += 1
