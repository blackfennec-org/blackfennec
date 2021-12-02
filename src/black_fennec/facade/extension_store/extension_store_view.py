import logging
from gi.repository import Gtk

from src.black_fennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel
from src.black_fennec.facade.extension_store.extension_view import ExtensionView
from src.black_fennec.facade.extension_store.extension_view_model import ExtensionViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/black_fennec/facade/extension_store/extension_store.glade')  # pylint:disable=line-too-long
class ExtensionStoreView(Gtk.ApplicationWindow):
    """Black Fennec Extension Store UI view"""
    __gtype_name__ = 'ExtensionStoreView'
    _extension_container = Gtk.Template.Child()

    def __init__(self, app, view_model: ExtensionStoreViewModel):
        super().__init__(application=app)
        logger.info('ExtensionStoreView __init__')
        view_model.bind(extensions=self.handle_extension_update)
        self._extension_index = {}
        self._extensions = set()
        self._view_model = view_model
        self.handle_extension_update(None, view_model.extensions)

    def handle_extension_update(self, unused_sender, extensions):
        intersection = self._extensions.intersection(extensions)
        to_be_added = extensions.difference(intersection)
        for extension in to_be_added:
            extension_view_model = ExtensionViewModel(
                extension, self._view_model.extension_api)
            extension_view = ExtensionView(extension_view_model)
            self._extension_container.add(extension_view)
            self._extension_index[extension] = extension_view

        to_be_deleted = self._extensions.difference(intersection)
        for extension in to_be_deleted:
            extension_view = self._extension_index[extension]
            self._extension_container.remove(extension_view.get_parent())

        self._extensions = extensions
