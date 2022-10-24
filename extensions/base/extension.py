from blackfennec.extension.extension_api import ExtensionApi
from base.date_time.date_time import DateTime
from base.date_time.date_time_view_factory import DateTimeViewFactory
from base.file.file_view_factory import FileViewFactory
from base.image.image_view_factory import ImageViewFactory
from blackfennec.interpretation.specification import Specification

__types = []


def _types(api: ExtensionApi):
    global __types
    if not __types:
        __types = [
            DateTime.TYPE,
            api.type_loader.load('base/file/file.json'),
            api.type_loader.load('base/image/image.json'),
        ]
    return __types


factories = [
    DateTimeViewFactory(),
    FileViewFactory(),
    ImageViewFactory(),
]


def create_extension(extension_api: ExtensionApi):
    """Registers all base types

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """

    for type in [DateTime.TYPE]:
        extension_api.type_registry.register_type(type)

    for type, factory in zip(_types(extension_api), factories):
        extension_api.view_factory_registry.register_view_factory(
            type, Specification(), factory)
        extension_api.view_factory_registry.register_view_factory(
            type, Specification(True), factory)


def destroy_extension(extension_api: ExtensionApi):
    """Deregisters all base types

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters
    """

    for type, factory in zip(_types(extension_api), factories):
        extension_api.type_registry.deregister_type(type)
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification())
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification(True))

    global __types
    __types = []
