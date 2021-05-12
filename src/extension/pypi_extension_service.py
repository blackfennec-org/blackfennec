# -*- coding: utf-8 -*-
import importlib
import subprocess
import sys

from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus


class PyPIExtensionService:
    @staticmethod
    def _list_extensions(location):
        extensions = subprocess.check_output([
            sys.executable,
            '-m',
            'pip',
            'freeze',
            '--location',
            location])
        installed_packages = [
            r.decode().split('==')[0]
            for r in extensions.split()
        ]
        return installed_packages

    def installed(self, sender, identifier, location): # pylint: disable=unused-argument
        extensions = dict()
        for extension_name in self._list_extensions(location):
            extension = Extension(
                self,
                sender,
                name=extension_name,
                location=location
            )
            extensions[extension_name] = extension
        return extensions

    @staticmethod
    def _install_extension(identifier, location, extension_name):
        command = [
            sys.executable,
            '-m',
            'pip',
            'install',
            '--extra-index-url',
            identifier,
            '--target=' + location,
            '--upgrade'
        ]
        command += extension_name
        subprocess.call(command)

    def load(self, extension):
        try:
            source = extension.source
            self._install_extension(
                source.identifier, source.location, extension.name
            )
            if source.target not in sys.path:
                sys.path.append(source.target)
            return importlib.import_module(extension.name, extension.name)
        except Exception as exception:
            extension.status = (ExtensionStatus.LOAD_FAILED, exception)
            raise exception
