import src.structure
from doubles.double_dummy import Dummy
from src.extension.extension import Extension
from src.extension.extension_api import ExtensionApi
from src.extension.extension_source import ExtensionSource
from src.extension.local_extension_service import LocalExtensionService
from src.extension.pypi_extension_service import PyPIExtensionService
from src.presentation.presenter_registry import PresenterRegistry
from src.structure.list import List
from src.structure.map import Map
from src.structure.string import String
from src.type_system.type_registry import TypeRegistry

if __name__ == '__main__':
    source_map = Map({
        ExtensionSource.SOURCE_IDENTIFICATION:
            String(src.presentation.__name__),
        ExtensionSource.SOURCE_LOCATION: List([
            String(path)
            for path in src.type_system.__path__
        ]),
        ExtensionSource.EXTENSION_LIST_KEY: List([
            Map({
                Extension.NAME_KEY:
                    String(src.presentation.column_based_presenter.__name__),
                Extension.LOCATION_KEY: List([
                    String(path)
                    for path
                    in src.presentation.column_based_presenter.__path__
                ])
            })
        ])
    })
    type_registry = TypeRegistry()
    presenter_registry = PresenterRegistry()
    extension_api = ExtensionApi(
        presenter_registry,
        type_registry,
        Dummy('NavigationService'),
        Dummy('InterpretationService')
    )
    local_extension_service = LocalExtensionService()
    external_extension_service = PyPIExtensionService()

    source = ExtensionSource(local_extension_service, source_map)
    source.load_extensions(extension_api)
    source.refresh_extensions()
