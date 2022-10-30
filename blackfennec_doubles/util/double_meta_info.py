
class MetaInfoMock:
    def __init__(self, version="0.0.0", description="description", name="BlackFennec", summary="summary", license="GPL-3", url="url"):
        self.name = name
        self.summary = summary
        self.version = version
        self.description = description
        self.license = license
        self.url = url
        self.version = version
        self.description = description

    def get_id(self):
        return self.name

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version

    def get_description(self):
        return self.description

    def get_authors(self):
        return self.name

    def get_summary(self):
        return self.summary

    def get_license(self):
        return self.license

    def get_home_page(self):
        return self.url

    def get_issue_page(self):
        return self.url

    def get_icon_path(self):
        return "face-monkey-symbolic"

    def get_copy_right(self) -> str:
        return f"© BlackFennec"
