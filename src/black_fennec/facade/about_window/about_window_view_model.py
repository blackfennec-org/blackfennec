from gi.repository import AppStream

from src.black_fennec.util.meta_info import BlackFennecMetaInfo


class AboutWindowViewModel:
    def __init__(self):
        self._meta_info = BlackFennecMetaInfo()
        self.version = self._meta_info.get_current_release().get_version()
        self.release_notes = self._meta_info.get_current_release().get_description()
        self.application_name = self._meta_info.component.get_name()
        self.developer_name = self._meta_info.component.get_developer_name()
        self.license = self._meta_info.component.get_project_license()
        self.comments = self._meta_info.get_plain_description()
        self.website = self._meta_info.component.get_url(AppStream.UrlKind.HOMEPAGE)
        self.issue_tracker = self._meta_info.component.get_url(AppStream.UrlKind.BUGTRACKER)
        self.copy_right = self._meta_info.get_copy_right()
        self.app_id = self._meta_info.component.get_id()
        self.icon = self._meta_info.get_icon_path()
