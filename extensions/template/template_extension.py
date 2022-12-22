
from blackfennec.extension_system import Extension
from blackfennec.extension_system import ExtensionApi


class TemplateExtension(Extension):
    def __init__(self, api: ExtensionApi):
        super().__init__(
            name='Extension Template',
            api=api)


def create(api: ExtensionApi) -> TemplateExtension:
    return TemplateExtension(api)
