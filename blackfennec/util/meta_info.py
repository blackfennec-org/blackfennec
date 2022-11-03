from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET

APPDATA_FILE = "org.blackfennec.app.metainfo.xml"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
META_INFO_DIR = Path("/app/")



class BlackFennecMetaInfo:
    def __init__(self):
        if (BASE_DIR / APPDATA_FILE).exists():
            meta_info_xml = str(BASE_DIR / APPDATA_FILE)
        elif (META_INFO_DIR / APPDATA_FILE).exists():
            meta_info_xml = str(META_INFO_DIR / APPDATA_FILE)
        else:
            raise AssertionError("file not found %s, %s", 
                BASE_DIR, META_INFO_DIR)
        

        self._xml = ET.parse(meta_info_xml)

    def get_app_id(self):
        return self._xml.find('id').text

    def get_name(self):
        return self._xml.find('name').text

    def get_summary(self):
        return self._xml.find('summary').text

    def get_version(self):
        return self._xml.find('releases/release').attrib['version']

    def get_release_notes(self) -> str:
        description = self._xml.find('releases/release/description/p')
        return ET.tostring(description).decode()

    def get_description(self):
        return self._xml.find('description/p').text

    def get_authors(self):
        return self._xml.find('developer_name').text.split(', ')

    def get_license(self):
        return self._xml.find('project_license').text

    def get_home_page(self):
        return self._xml.find('url[@type="homepage"]').text

    def get_issue_page(self):
        return self._xml.find('url[@type="bugtracker"]').text
  
    def get_icon_path(self) -> str:
        return str(BASE_DIR.joinpath('icon.png'))

    def get_copy_right(self) -> str:
        return f"© {datetime.now().year} {self.get_name()}"

