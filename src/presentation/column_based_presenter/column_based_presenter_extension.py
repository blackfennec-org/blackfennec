from src.extension.extension_api import ExtensionApi
from src.presentation.column_based_presenter.column_based_presenter_view_factory import ColumnBasedPresenterViewFactory


def create_extension(extension_api: ExtensionApi):
    extension_api.presenter_registry.register_presenter(
        ColumnBasedPresenterViewFactory(
            extension_api.interpretation_service))


def destroy_extension(extension_api: ExtensionApi):
    extension_api.presenter_registry.deregister_presenter(
        ColumnBasedPresenterViewFactory
    )
