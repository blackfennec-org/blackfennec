

class ObservableLayerMock:

    def __init__(self):
        self.change_notifications = []

    def on_changed(self, sender, notification):
        self.change_notifications.append(notification)