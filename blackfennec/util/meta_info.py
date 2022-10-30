from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parent.parent.parent
META_INFO_XML = str(BASE_DIR.joinpath('org.blackfennec.app.metainfo.xml'))


class BlackFennecMetaInfo:
    def __init__(self):
        self._xml = ET.parse(META_INFO_XML)

    def get_app_id(self):
        self._xml.find('id').text

    def get_name(self):
        self._xml.find('name').text

    def get_summary(self):
        self._xml.find('summary').text

    def get_version(self):
        self._xml.find('releases/release').attrib['version']

    def get_description(self):
        self._xml.find('description').text

    def get_authors(self):
        self._xml.find('developer_name').text.split(', ')

    def get_license(self):
        self._xml.find('project_license').text

    def get_comments(self) -> list[str]:
        return []

    def get_home_page(self):
        self._xml.find('url[@type="homepage"]').text

    def get_issue_page(self):
        self._xml.find('url[@type="bugtracker"]').text
  
    def get_icon_path(self) -> str:
        return str(BASE_DIR.joinpath('icon.png'))

    def get_copy_right(self) -> str:
        return f"© {datetime.now().year} {self.get_name()}"
