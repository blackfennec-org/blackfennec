from src.extension.extension_api import ExtensionApi
from src.visualisation.core.boolean.boolean_bidder import BooleanBidder
from src.visualisation.core.list.list_bidder import ListBidder
from src.visualisation.core.map.map_bidder import MapBidder
from src.visualisation.core.number.number_bidder import NumberBidder
from src.visualisation.core.reference.reference_bidder import ReferenceBidder
from src.visualisation.core.string.string_bidder import StringBidder


def create_extension(extension_api: ExtensionApi):
    """Registers all core types in type registry.
    
    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """
    extension_api.type_registry.register_type(BooleanBidder())
    extension_api.type_registry.register_type(NumberBidder())
    extension_api.type_registry.register_type(StringBidder())
    extension_api.type_registry.register_type(
        ListBidder(extension_api.interpretation_service)
    )
    extension_api.type_registry.register_type(
        MapBidder(extension_api.interpretation_service)
    )
    extension_api.type_registry.register_type(ReferenceBidder())


def destroy_extension(extension_api: ExtensionApi):
    extension_api.type_registry.deregister_type(BooleanBidder)
    extension_api.type_registry.deregister_type(NumberBidder)
    extension_api.type_registry.deregister_type(StringBidder)
    extension_api.type_registry.deregister_type(ListBidder)
    extension_api.type_registry.deregister_type(MapBidder)
    extension_api.type_registry.deregister_type(ReferenceBidder)
