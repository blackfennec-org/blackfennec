# -*- coding: utf-8 -*-
import importlib
import pkgutil

from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus


class LocalExtensionService:
    @staticmethod
    def _iter_namespace(name, location):
        return pkgutil.iter_modules(
            location,
            name + ".")

    def installed(self, sender, name, location):
        extensions = dict()
        for module_info in self._iter_namespace(name, location):
            module_name = module_info.name
            module_spec = module_info.module_finder.find_spec(module_name)
            print(module_spec)
            module_path = module_spec.submodule_search_locations
            extension = Extension(
                self,
                sender,
                name=module_name,
                location=module_path
            )
            extensions[module_name] = extension
        return extensions

    @staticmethod
    def load(extension: Extension):
        try:
            return importlib.import_module(extension.name)
        except Exception as exception:
            extension.status = (ExtensionStatus.LOAD_FAILED, exception)
            raise exception
