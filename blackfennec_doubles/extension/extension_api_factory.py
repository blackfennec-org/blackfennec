from blackfennec.extension.extension_api import ExtensionApi
from blackfennec_doubles.double_dummy import Dummy


def create_extension_api(**kwargs):
    args = {
        'presenter_registry': Dummy('PresenterRegistry'),
        'type_registry': Dummy('TypeRegistry'),
        'interpretation_service': Dummy('InterpretationService'),
        'view_factory': Dummy('ViewFactory'),
        'view_factory_registry': Dummy('ViewFactoryRegistry'),
        'type_loader': Dummy('TypeLoader'),
        'action_registry': Dummy('ActionRegistry'),
        'document_registry': Dummy('DocumentRegistry'),
        'document_factory': Dummy('DocumentFactory'),
        'ui_service': Dummy('UiService'),
        'mime_type_registry': Dummy('MimeTypeRegistry'),
    }
    args.update(kwargs)

    return ExtensionApi(
        **args
    )
