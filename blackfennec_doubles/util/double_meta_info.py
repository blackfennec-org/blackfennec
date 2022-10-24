class ReleaseMock:
    def __init__(self, version, description):
        self.version = version
        self.description = description

    def get_version(self):
        return self.version

    def get_description(self):
        return self.description


class ComponentMock:
    def __init__(self, name="BlackFennec", summary="summary", project_license="GPL3", url="url"):
        self.name = name
        self.summary = summary
        self.project_license = project_license
        self.url = url

    def get_name(self):
        return self.name

    def get_developer_name(self):
        return self.name

    def get_summary(self):
        return self.summary

    def get_project_license(self):
        return self.project_license

    def get_url(self, url_kind):
        return self.url

    def get_id(self):
        return self.name


class MetaInfoMock:
    def __init__(self, component=None, release_version="0.0.0", description="description"):
        self.release_version = release_version
        self.release_description = description
        self.description = description
        self.component = component or ComponentMock()

    def get_current_release(self):
        return ReleaseMock(self.release_version, self.release_description)

    def get_plain_description(self):
        return self.description

    def get_icon_path(self):
        return "face-monkey-symbolic"
