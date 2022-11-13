# -*- coding: utf-8 -*-
import os
import importlib
import inspect
import logging
import pkgutil
from importlib.metadata import entry_points

from blackfennec.extension.extension import Extension
from blackfennec.extension.extension_status import ExtensionStatus

logger = logging.getLogger(__name__)


class LocalExtensionService:
    """
    Can import and list modules present in a local
        python namespace.
    """

    @classmethod
    def _validate_extension(self, module) -> bool:
        logger.debug(f'Validating module {module}')
        if not self._function_exists(module, 'create_extension'):
            return False
        if not self._function_exists(module, 'destroy_extension'):
            return False
        return True

    def _function_exists(module, function_name):
        members = inspect.getmembers(module)
        for function, _ in members:
            if function == function_name:
                return True
        return False

    def installed(
            self,
            sender: 'ExtensionSource',
            name: str,
            locations: list[str]
    ) -> list[Extension]:
        """
        Args:
            sender (ExtensionSource): source querying extensions
            name (str): name of namespace
            location (str): location of namespace
        Returns:
            [Extension]: Extensions which are installed in namespace
                and have a create_extension and destroy_extension
                method
        """
        extensions = {}
        modules = entry_points(group="blackfennec.extension")
        logger.debug(f"Found {len(modules)} modules")
        for module in reversed(modules):
            logger.debug(f'Found module {module.name}: {module}')
            if not self._validate_extension(module.load()):
                message = f'module "{module.name}" is not a valid extension'
                logger.warning(message)
                continue
            extension = Extension(
                self,
                sender,
                name=module.name
            )
            extensions[module.name] = extension
        return extensions

    @staticmethod
    def load(extension: Extension):
        try:
            return importlib.import_module(extension.name)
        except Exception as exception:
            extension.status = (ExtensionStatus.LOAD_FAILED, exception)
            raise exception
