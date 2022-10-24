from datetime import datetime
from functools import lru_cache
from pathlib import Path

from gi.repository import AppStream, Gio

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
META_INFO_XML = str(BASE_DIR.joinpath('org.blackfennec.app.metainfo.xml'))


class BlackFennecMetaInfo:
    def __init__(self):
        meta_info_file = Gio.File.new_for_path(META_INFO_XML)
        meta_data = AppStream.Metadata.new()
        meta_data.parse_file(meta_info_file, AppStream.FormatKind.XML)
        self._component = meta_data.get_component()

    @property
    def component(self) -> AppStream.Component:
        return self._component

    @lru_cache
    def get_current_release(self) -> AppStream.Release:
        releases = self.component.get_releases()
        current_release = releases[0]
        for release in releases:
            if release.vercmp(current_release) == 1:
                current_release = release
        return current_release

    def get_icon_path(self) -> str:
        return str(BASE_DIR.joinpath('icon.png'))

    def get_plain_description(self) -> str:
        return AppStream.markup_convert_simple(self._component.get_description())

    def get_copy_right(self) -> str:
        return f"© {datetime.now().year} {self.component.get_name()}"

    def get_authors(self) -> []:
        return self.component.get_developer_name().split(', ')
