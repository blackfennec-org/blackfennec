#!/usr/bin/env python3

import logging
import os
import sys

from blackfennec.facade.main_window.black_fennec_view import BlackFennecView
from blackfennec.facade.main_window.black_fennec_view_model import \
    BlackFennecViewModel
from blackfennec.util.initialisation_service import InitialisationService

from gi.repository import Adw, Gio, Gtk

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

CONFIG_HOME = os.path.expanduser('~/.config/blackfennec/')
if not os.path.exists(CONFIG_HOME):
    os.makedirs(CONFIG_HOME)
EXTENSIONS = os.path.join(CONFIG_HOME, os.path.relpath('extensions.json'))

sys.path.append('/app/extensions/lib/python3.10/site-packages')


class BlackFennecApp(Adw.Application):
    def __init__(self, initialisation_service: InitialisationService):
        super().__init__(application_id='org.blackfennec.app')
        self.services = initialisation_service
        self.win = None
        self._view_model = None

        self.connect('activate', self.on_activate)
        self.connect('open', self.on_open)
        self.set_flags(Gio.ApplicationFlags.HANDLES_OPEN)

    def create_main_window(self, app):
        self._view_model = BlackFennecViewModel(self.services.extension_api)
        return BlackFennecView(app, self._view_model, self.services.ui_service)

    def on_activate(self, app):
        if not self.win:
            self.win = self.create_main_window(app)
        self.win.present()

    def on_open(self, app, files, n_files, hint):
        self.on_activate(app)
        for file in files:
            self._view_model.open(file.get_path())


def main(argv):
    initialisation_service = InitialisationService(
        extension_configuration_file=EXTENSIONS
    )
    app = BlackFennecApp(initialisation_service)
    app.run(argv)


if __name__ == '__main__':
    main(sys.argv)
