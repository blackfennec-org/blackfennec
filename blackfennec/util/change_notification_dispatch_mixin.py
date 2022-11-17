import logging

from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class ChangeNotificationDispatchMixin(Observable):
    """Mixin class for dispatching change notifications."""

    def __init__(self):
        super().__init__()

    def _dispatch_change_notification(self, sender, notification):
        if notification.new_value != notification.old_value:
            self._notify('changed', notification.new_value, sender)
        else:
            logger.info('No change in value, not notifying')
