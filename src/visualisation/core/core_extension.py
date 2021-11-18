from src.extension.extension_api import ExtensionApi
from src.visualisation.core.boolean.boolean_bidder import BooleanBidder
from src.visualisation.core.boolean.boolean_template import BooleanTemplate
from src.visualisation.core.list.list_bidder import ListBidder
from src.visualisation.core.list.list_template import ListTemplate
from src.visualisation.core.map.map_bidder import MapBidder
from src.visualisation.core.map.map_template import MapTemplate
from src.visualisation.core.number.number_bidder import NumberBidder
from src.visualisation.core.number.number_template import NumberTemplate
from src.visualisation.core.reference.reference_bidder import ReferenceBidder
from src.visualisation.core.reference.reference_template import ReferenceTemplate
from src.visualisation.core.string.string_bidder import StringBidder
from src.visualisation.core.string.string_template import StringTemplate


def create_extension(extension_api: ExtensionApi):
    """
    Registers all core types in black-fennec
    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters.
    """
    extension_api.type_registry.register_type(BooleanBidder())
    extension_api.template_registry.register_template(BooleanTemplate())

    extension_api.type_registry.register_type(NumberBidder())
    extension_api.template_registry.register_template(NumberTemplate())

    extension_api.type_registry.register_type(StringBidder())
    extension_api.template_registry.register_template(StringTemplate())

    extension_api.type_registry.register_type(
        ListBidder(
            extension_api.interpretation_service,
            extension_api.template_registry
        )
    )
    extension_api.template_registry.register_template(ListTemplate())

    extension_api.type_registry.register_type(
        MapBidder(
            extension_api.interpretation_service,
            extension_api.template_registry))
    extension_api.template_registry.register_template(MapTemplate())

    extension_api.type_registry.register_type(ReferenceBidder())
    extension_api.template_registry.register_template(ReferenceTemplate())


def destroy_extension(extension_api: ExtensionApi):
    """
    Deregisters all core types from black-fennec
    Args:
        extension_api (ExtensionApi): contains constructor injection
            parameters
    """
    extension_api.type_registry.deregister_type(BooleanBidder)
    extension_api.template_registry.deregister_template(BooleanTemplate)

    extension_api.type_registry.deregister_type(NumberBidder)
    extension_api.template_registry.deregister_template(NumberTemplate)

    extension_api.type_registry.deregister_type(StringBidder)
    extension_api.template_registry.deregister_template(StringTemplate)

    extension_api.type_registry.deregister_type(ListBidder)
    extension_api.template_registry.deregister_template(ListTemplate)

    extension_api.type_registry.deregister_type(MapBidder)
    extension_api.template_registry.deregister_template(MapTemplate)

    extension_api.type_registry.deregister_type(ReferenceBidder)
    extension_api.template_registry.deregister_template(ReferenceTemplate)
