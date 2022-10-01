from src.extension.extension_api import ExtensionApi
from src.visualisation.base.address.address import Address
from src.visualisation.base.date_time.date_time import DateTime
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange
from src.visualisation.base.file.file import File
from src.visualisation.base.image.image import Image
from src.visualisation.base.person.person import Person
from src.visualisation.base.address.address_view_factory import AddressViewFactory
from src.visualisation.base.date_time.date_time_view_factory import DateTimeViewFactory
from src.visualisation.base.date_time_range.date_time_range_view_factory import DateTimeRangeViewFactory
from src.visualisation.base.file.file_view_factory import FileViewFactory
from src.visualisation.base.image.image_view_factory import ImageViewFactory
from src.visualisation.base.person.person_view_factory import PersonViewFactory
from src.black_fennec.interpretation.specification import Specification


types = [
    Address.TYPE,
    DateTime.TYPE,
    DateTimeRange.TYPE,
    File.TYPE,
    Image.TYPE,
    Person.TYPE
]

factories = [
    AddressViewFactory(),
    DateTimeViewFactory(),
    DateTimeRangeViewFactory(),
    FileViewFactory(),
    ImageViewFactory(),
    PersonViewFactory(),
]

def create_extension(extension_api: ExtensionApi):
    """Registers all base types

    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """

    for type, factory in zip(types, factories):
        extension_api.type_registry.register_type(type)
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


    for type, factory in zip(types, factories):
        extension_api.type_registry.deregister_type(type)
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification())
        extension_api.view_factory_registry.deregister_view_factory(
            type, Specification(True))

