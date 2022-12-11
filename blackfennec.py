#!/usr/bin/env python3

import logging
import sys
from blackfennec.extension.extension_service import ExtensionService

from blackfennec.facade.main_window.black_fennec_view import BlackFennecView
from blackfennec.facade.main_window.black_fennec_view_model import \
    BlackFennecViewModel
from blackfennec.util.service_locator import ServiceLocator

from gi.repository import Adw, Gio

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

sys.path.append('/app/extensions/lib/python3.10/site-packages')


class BlackFennecApp(Adw.Application):
    def __init__(self, services: ServiceLocator):
        super().__init__(application_id='org.blackfennec.app')
        self.services = services
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
    services = ServiceLocator()
    ExtensionService.load(
        services.extension_api, 
        services.extension_registry)
    app = BlackFennecApp(services)
    app.run(argv)


if __name__ == '__main__':
    main(sys.argv)
