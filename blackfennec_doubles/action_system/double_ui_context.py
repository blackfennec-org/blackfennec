class UiContextMock:
    def __init__(self, root):
        self.root = root
        self.get_root_count = 0

    def get_root(self):
        self.get_root_count += 1
        return self.root
