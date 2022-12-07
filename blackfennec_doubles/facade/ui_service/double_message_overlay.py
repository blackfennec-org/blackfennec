from blackfennec_doubles.actions.double_ui_context import UiContextMock


class MessageOverlayMock:
    def __init__(self, root=None):
        self.add_toast_parameter = None
        self.add_toast_count = 0
        self.root = root or UiContextMock('root')

    def add_toast(self, toast):
        self.add_toast_parameter = toast
        self.add_toast_count += 1

    def get_root(self):
        return self.root
