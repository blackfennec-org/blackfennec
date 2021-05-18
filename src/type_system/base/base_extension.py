from src.extension.extension_api import ExtensionApi
from src.type_system.base.address.address_bidder import AddressBidder
from src.type_system.base.date_time.date_time_bidder import DateTimeBidder
from src.type_system.base.date_time_range.date_time_range_bidder import DateTimeRangeBidder
from src.type_system.base.file.file_bidder import FileBidder
from src.type_system.base.image.image_bidder import ImageBidder
from src.type_system.base.person.person_bidder import PersonBidder


def create_extension(extension_api: ExtensionApi):
    extension_api.type_registry.register_type(AddressBidder())
    extension_api.type_registry.register_type(DateTimeBidder())
    extension_api.type_registry.register_type(DateTimeRangeBidder())
    extension_api.type_registry.register_type(FileBidder())
    extension_api.type_registry.register_type(ImageBidder())
    extension_api.type_registry.register_type(PersonBidder())


def destroy_extension(extension_api: ExtensionApi):
    raise NotImplementedError('Not implemented yet')
