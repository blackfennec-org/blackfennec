#!/usr/bin/env python3

import logging
import sys
from blackfennec.extension.extension_service import ExtensionService

from blackfennec.presentation_system.main_window.black_fennec_view import BlackFennecView
from blackfennec.presentation_system.main_window.black_fennec_view_model import \
    BlackFennecViewModel
from blackfennec.util.service_locator import ServiceLocator
from blackfennec.extension.extension import Extension
from blackfennec.presentation_system.extension_warning_dialog.extension_warning_dialog import \
    ExtensionWarningDialog

from gi.repository import Adw, Gio

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

sys.path.append('/app/extensions/lib/python3.10/site-packages')


class BlackFennecApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id='org.blackfennec.app')

        self.services = ServiceLocator()
        self.win = None
        self._view_model = None

        self.connect('activate', self.on_activate)
        self.connect('open', self.on_open)
        self.set_flags(Gio.ApplicationFlags.HANDLES_OPEN)

        self.load_extensions()

    def create_main_window(self, app):
        self._view_model = BlackFennecViewModel(self.services)
        return BlackFennecView(app, self._view_model, self.services.ui_service)

    def create_extension_warning_dialog(self, recommended_extension_names):
        dialog = ExtensionWarningDialog(
            recommended_extension_names, transient_for=self.win)
        dialog.show()

    def on_activate(self, app):
        if not self.win:
            self.win = self.create_main_window(app)
            self.check_extensions()
        self.win.present()

    def on_open(self, app, files, n_files, hint):
        self.on_activate(app)
        for file in files:
            self._view_model.open(file.get_path())

    def load_extensions(self):
        ExtensionService.load(
            self.services.extension_api,
            self.services.extension_registry)

    def check_extensions(self):
        extensions = self.services.extension_registry.get_extensions()
        recommended_extension_names = ["core", "base"]
        for extension in extensions:
            if extension.name in recommended_extension_names:
                if extension.state == Extension.State.ACTIVE:
                    recommended_extension_names.remove(extension.name)
        if recommended_extension_names:
            logger.warning(
                f"Recommended extensions not activated: {recommended_extension_names}"
            )
            self.create_extension_warning_dialog(recommended_extension_names)


def main(argv):
    app = BlackFennecApp()
    app.run(argv)


if __name__ == '__main__':
    main(sys.argv)
