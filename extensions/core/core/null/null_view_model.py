from blackfennec.structure.null import Null
from blackfennec.util.change_notification_dispatch_mixin import \
    ChangeNotificationDispatchMixin


class NullViewModel(ChangeNotificationDispatchMixin):
    def __init__(self, interpretation):
        super().__init__()

        self._null = interpretation.structure
        self._null.bind(changed=self._dispatch_change_notification)

    @property
    def null(self) -> Null:
        """Property for value of type number.Number"""
        return self._null

    @null.setter
    def null(self, null: Null):
        self._null = null
