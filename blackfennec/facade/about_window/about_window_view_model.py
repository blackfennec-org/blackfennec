from blackfennec.util.meta_info import BlackFennecMetaInfo


class AboutWindowViewModel:
    def __init__(self):
        self._meta_info = BlackFennecMetaInfo()
        self.app_id = self._meta_info.get_app_id()
        self.application_name = self._meta_info.get_name()
        self.version = self._meta_info.get_version()
        self.release_notes = self._meta_info.get_description()
        self.developer_names = self._meta_info.get_authors()
        self.license = self._meta_info.get_license()
        self.comments = self._meta_info.get_comments()
        self.website = self._meta_info.get_home_page()
        self.issue_tracker = self._meta_info.get_issue_page()
        self.copy_right = self._meta_info.get_copy_right()
        self.icon = self._meta_info.get_icon_path()
