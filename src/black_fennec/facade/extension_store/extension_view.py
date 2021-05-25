import logging
from gi.repository import Gtk

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/black_fennec/facade/extension_store/extension.glade')
class ExtensionView(Gtk.ApplicationWindow):
    """Black Fennec Extension view"""
    __gtype_name__ = 'ExtensionView'
    _name = Gtk.Template.Child()
    _description = Gtk.Template.Child()
    _button = Gtk.Template.Child()

    def __init__(self, app=None):
        super().__init__(application=app)
        logger.info('ExtensionView __init__')
        name = ""
        description = ""
        self._name.set_text(name)
        self._description.set_text(description, len(description.encode('utf-8')))

    @Gtk.Template.Callback()
    def _on_button_clicked(self, unused_sender):
        enable = self.toggle_button()
        #self._view_model.new()
        logger.debug('new clicked')

    def toggle_button(self):
        text = self._button.get_test()
        if text == 'Enable':
            self._button.set_test('Disable')
            return True
        else:
            self._button.set_test('Enable')
            return False
