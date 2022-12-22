
from blackfennec.extension_system import Extension
from blackfennec.extension_system import ExtensionApi


class MyExtension(Extension):
    def __init__(self, api: ExtensionApi):
        super().__init__(
            name='My Extension', 
            api=api)


def create(api: ExtensionApi) -> MyExtension:
    return MyExtension(api)
