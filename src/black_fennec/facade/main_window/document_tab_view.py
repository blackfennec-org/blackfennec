import logging
import threading
import traceback

from gi.repository import Adw, GLib

from src.black_fennec.facade.main_window.document_tab import DocumentTab

logger = logging.getLogger(__name__)


class DocumentTabView():
    def __init__(self, tab_view: Adw.TabView, tab: DocumentTab):
        error_occured = False
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
            error_occured = True

        self.tab_page = tab_view.add_page(presenter)
        self.tab_page.set_title(tab.uri)
        self.tab_page.set_tooltip(tab.uri)
        self.tab_page.document_tab = tab

        if not error_occured:
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
