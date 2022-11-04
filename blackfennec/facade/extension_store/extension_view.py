import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from blackfennec.facade.extension_store.extension_view_model import ExtensionViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('extension.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ExtensionView(Adw.Bin):
    """Black Fennec Extension view"""
    __gtype_name__ = 'ExtensionView'
    _name: Gtk.Label = Gtk.Template.Child()
    _description = Gtk.Template.Child()
    _button = Gtk.Template.Child()

    def __init__(self, view_model: ExtensionViewModel):
        super().__init__()
        logger.info('ExtensionView __init__')
        self._view_model = view_model

        name = view_model.name
        description = view_model.description
        self._name.set_text(name)
        self._description.set_text(
            description,
            len(description.encode('utf-8'))
        )

        self._update_button_text()

    @Gtk.Template.Callback()
    def _on_button_clicked(self, unused_sender):
        self.toggle_button()
        logger.debug('new clicked')

    def toggle_button(self):
        text = self._button.get_label()
        if text == 'Enable':
            self._view_model.enable()
            self._update_button_text()
        else:
            self._view_model.disable()
            self._update_button_text()

    def _update_button_text(self):
        enabled = self._view_model.enabled
        if enabled:
            self._button.set_label('Disable')
        else:
            self._button.set_label('Enable')