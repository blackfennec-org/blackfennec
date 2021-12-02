# -*- coding: utf-8 -*-
import importlib
import inspect
import logging
import pkgutil

from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus

logger = logging.getLogger(__name__)


class LocalExtensionService:
    """
    Can import and list modules present in a local
        python namespace.
    """

    @staticmethod
    def _iter_namespace(name, location):
        return pkgutil.iter_modules(
            location,
            name + '.')

    @staticmethod
    def _check_if_function_exists(module, function_name):
        members = inspect.getmembers(module)
        for function, _ in members:
            if function == function_name:
                return True
        return False

    def installed(
            self,
            sender: 'ExtensionSource',
            name: str,
            location: [str]
    ) -> [Extension]:
        """
        Args:
            sender (ExtensionSource): source querying extensions
            name (str): name of namespace
            location ([str]): location of namespace
        Returns:
            [Extension]: Extensions which are installed in namespace
                and have a create_extension and destroy_extension
                method
        """
        extensions = {}
        for module_structure in self._iter_namespace(name, location):
            module_name = module_structure.name
            module_spec = module_structure.module_finder.find_spec(module_name)
            module_path = module_spec.submodule_search_locations
            extension = Extension(
                self,
                sender,
                name=module_name,
                location=module_path
            )
            module = importlib.import_module(module_name)
            if self._check_if_function_exists(
                    module, 'create_extension') and self._check_if_function_exists(
                    module, 'destroy_extension'):
                extensions[module_name] = extension
            else:
                message = f'module({module_name}, {module_path}) does ' \
                          f'not contain create_extension and' \
                          f' destroy_extension function'
                logger.info(message)
        return extensions

    @staticmethod
    def load(extension: Extension):
        try:
            return importlib.import_module(extension.name)
        except Exception as exception:
            extension.status = (ExtensionStatus.LOAD_FAILED, exception)
            raise exception
