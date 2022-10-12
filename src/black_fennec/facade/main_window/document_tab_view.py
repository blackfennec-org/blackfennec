import logging
import traceback

from gi.repository import Adw

logger = logging.getLogger(__name__)


class DocumentTabView():
    def __init__(self, tab_view: Adw.TabView, tab):
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

        if not error_occured:
            self.tab_page.set_loading(True)
            try:
                tab.load_document()
                self.tab_page.set_loading(False)
            except Exception as e:
                logger.error(traceback.format_exc())
                self.tab_page.set_loading(False)
                presenter.set_error(str(e))
                return
