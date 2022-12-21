import logging
import threading
import traceback

from gi.repository import Adw, GLib, Gio

from blackfennec.presentation_system.main_window.document_tab import DocumentTab

logger = logging.getLogger(__name__)


class DocumentTabView:
    def __init__(self, tab_view: Adw.TabView, tab: DocumentTab):
        error_occurred = False
        try:
            presenter = tab.create_presenter()
        except Exception as e:
            logger.error(traceback.format_exc())
            presenter = Adw.StatusPage(
                title='Error',
                description='An error occurred while creating the presenter for this tab',
                icon_name='computer-fail-symbolic'
            )
            presenter.set_hexpand(True)
            error_occurred = True

        self.tab_page = tab_view.add_page(presenter)
        self.tab_page.document_tab = tab
        self.tab_page.document_tab.bind(
            title=self._on_title_changed,
            icon=self._on_icon_changed,
            uri=self._on_uri_changed
        )
        self._on_title_changed(self, tab.title)
        self._on_icon_changed(self, tab.icon)
        self._on_uri_changed(self, tab.uri)

        if not error_occurred:
            self.tab_page.set_loading(True)

            def load_document_async():
                try:
                    document = tab.load_document()

                    def set_presenter():
                        if tab.presenter:
                            tab.presenter.set_structure(document)
                        else:
                            message = "Presenter not set yet"
                            logger.warning(message)
                            raise RuntimeError(message)

                    GLib.idle_add(set_presenter)
                    GLib.idle_add(lambda: self.tab_page.set_loading(False))
                except Exception as e:
                    message = traceback.format_exc()
                    logger.error(message)
                    GLib.idle_add(lambda: self.tab_page.set_loading(False))
                    GLib.idle_add(lambda: presenter.set_error(message))
                    return False

            threading.Thread(target=load_document_async).start()

    def _on_title_changed(self, unused_sender, title: str):
        self.tab_page.set_title(title)

    def _on_icon_changed(self, unused_sender, icon: str):
        self.tab_page.set_icon(Gio.Icon.new_for_string(icon))

    def _on_uri_changed(self, unused_sender, uri: str):
        self.tab_page.set_tooltip(uri)
