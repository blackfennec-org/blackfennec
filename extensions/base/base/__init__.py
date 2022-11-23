from pathlib import Path
from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.interpretation.specification import Specification
from base.date_time.date_time import DateTime

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from base.date_time.date_time_view_factory import DateTimeViewFactory
from base.file.file_view_factory import FileViewFactory
from base.image.image_view_factory import ImageViewFactory

BASE_NAME = Path(__file__).parent.as_posix()
__types = []


def _types(api: ExtensionApi):
    global __types
    if not __types:
        __types = [
            DateTime.TYPE,
            api.type_loader.load(BASE_NAME + '/file/file.json'),
            api.type_loader.load(BASE_NAME + '/image/image.json'),
        ]
    return __types


def create_extension(extension_api: ExtensionApi):
    """Registers all base types

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """

    factories = [
        DateTimeViewFactory(),
        FileViewFactory(extension_api.document_registry),
        ImageViewFactory(extension_api.document_registry),
    ]

    for type in [DateTime.TYPE]:
        extension_api.type_registry.register_type(type)

    for type, factory in zip(_types(extension_api), factories):
        for specification in [Specification(), Specification(request_preview=True)]:
            if factory.satisfies(specification):
                extension_api.view_factory_registry.register_view_factory(
                    type, specification, factory)


def destroy_extension(extension_api: ExtensionApi):
    """Deregisters all base types

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters
    """

    for type in _types(extension_api):
        extension_api.type_registry.deregister_type(type)
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification())
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification(True))

    global __types
    __types = []
