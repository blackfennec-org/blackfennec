from gi.repository import Adw

from blackfennec.facade.about_window.about_window_view_model import AboutWindowViewModel


class AboutWindowView:

    def __init__(self, view_model: AboutWindowViewModel, parent_window):
        self._view_model = view_model
        self.adw_about_window = Adw.AboutWindow()
        self.adw_about_window.set_transient_for(parent_window)
        self.adw_about_window.set_application_name(self._view_model.name)
        self.adw_about_window.set_comments(self._view_model.comments)
        self.adw_about_window.set_version(self._view_model.version)
        self.adw_about_window.set_release_notes(self._view_model.release_notes)
        self.adw_about_window.set_website(self._view_model.website)
        if self._view_model.issue_tracker:
            self.adw_about_window.set_issue_url(self._view_model.issue_tracker)
        self.adw_about_window.set_license(self._view_model.license)
        self.adw_about_window.set_copyright(self._view_model.copy_right)
        self.adw_about_window.set_icon_name(self._view_model.icon)
        self.adw_about_window.set_developers(self._view_model.developer_names)
