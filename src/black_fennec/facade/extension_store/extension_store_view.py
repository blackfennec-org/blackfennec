import logging
from gi.repository import Gtk

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/black_fennec/facade/extension_store/extension_store.glade')
class ExtensionStoreView(Gtk.ApplicationWindow):
    """Black Fennec Extension Store UI view"""
    __gtype_name__ = 'ExtensionStoreView'

    def __init__(self, app=None):
        super().__init__(application=app)
        logger.info('ExtensionStoreView __init__')
