import os
from gi.repository import Adw, Gtk


class ExtensionWarningDialog(Adw.MessageDialog):
    def __init__(self, missing, **kwargs):
        super().__init__(**kwargs)

        self.set_heading(heading='Missing Recommended Extensions')
        self.set_body(
            body='Black Fennec has detected that some recommended extensions '
                + 'are currently not installed. '
                + 'The missing recommended extensions are:\n - '
                + "\n - ".join(missing))
        self.add_response(Gtk.ResponseType.CANCEL.value_nick, 'I know, cancel')
        self.set_response_appearance(
            response=Gtk.ResponseType.CANCEL.value_nick,
            appearance=Adw.ResponseAppearance.DESTRUCTIVE
        )
        self.add_response(Gtk.ResponseType.OK.value_nick, 'Install')
        self.set_response_appearance(
            response=Gtk.ResponseType.OK.value_nick,
            appearance=Adw.ResponseAppearance.SUGGESTED
        )
        self.connect('response', self.dialog_response)

    def dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK.value_nick:
            self.destroy()
            os.system('xdg-open /app/org.blackfennec.app.flatpakref')
        elif response == Gtk.ResponseType.CANCEL.value_nick:
            self.destroy()
