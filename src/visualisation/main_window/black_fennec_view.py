import logging
from gi.repository import Gtk

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/main_window/black_fennec.glade')
class BlackFennecView(Gtk.ApplicationWindow):
    """Black Fennec Main UI view"""
    __gtype_name__ = 'BlackFennecView'
    _presenter_container = Gtk.Template.Child()

    def __init__(self, app, view_model):
        super().__init__(application=app)
        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._presenter_container.add(self._view_model.presenter)
        self._presenter_container.show_all()

    @Gtk.Template.Callback()
    def on_new_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.new()
        logger.debug('new clicked')

    @Gtk.Template.Callback()
    def on_open_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        logger.debug('open clicked')
        dialog = Gtk.FileChooserDialog(
            title='Please choose a file',
            parent=self,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = dialog.get_filename()
            self._view_model.open(filename)
        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('file selection canceled')

        dialog.destroy()


    @Gtk.Template.Callback()
    def on_quit_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.quit()
        logger.debug('quit clicked')

    @Gtk.Template.Callback()
    def on_save_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.save()
        logger.debug('save clicked')

    @Gtk.Template.Callback()
    def on_save_as_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.save_as()
        logger.debug('save as clicked')

    @Gtk.Template.Callback()
    def on_go_to_store_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.go_to_store()
        logger.debug('go to store clicked')

    @Gtk.Template.Callback()
    def on_about_and_help_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.about_and_help()
        logger.debug('about and help clicked')


