import logging
from gi.repository import Gtk, Gdk

logger = logging.getLogger(__name__)


@Gtk.Template(filename="src/black_fennec.glade")
class BlackFennecView(Gtk.ApplicationWindow):
    """Black Fennec Main UI view"""
    __gtype_name__ = 'BlackFennecView'
    _presenter_container = Gtk.Template.Child()

    def __init__(self, app, view_model, click_handler=None):

        super().__init__(application=app)
        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._presenter_container.add(self._view_model.presenter)
        self._presenter_container.show_all()

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path('src/style.css')
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider, 
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self._click_handler = click_handler

    def _click_handler(self) -> None:
        """Handles clicks on items"""

    @Gtk.Template.Callback()
    def on_new_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.new()
        logger.debug('new clicked')

    @Gtk.Template.Callback()
    def on_open_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.open()
        logger.debug('open clicked')

    @Gtk.Template.Callback()
    def on_quit_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.quit()
        logger.debug('quit clicked')

    @Gtk.Template.Callback()
    def on_save_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.save()
        logger.debug('save clicked')

    @Gtk.Template.Callback()
    def on_save_as_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.save_as()
        logger.debug('save as clicked')

    @Gtk.Template.Callback()
    def on_go_to_store_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.go_to_store()
        logger.debug('go to store clicked')

    @Gtk.Template.Callback()
    def on_about_and_help_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._view_model.about_and_help()
        logger.debug('about and help clicked')


