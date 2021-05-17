# -*- coding: utf-8 -*-
import importlib
import subprocess
import sys
from typing import Any

from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus


class PyPIExtensionService:
    """
    PyPI extension service

    Queries extensions installed and
        installs/loads extensions
    """

    @staticmethod
    def _list_extensions(location) -> [str]:
        """
        Queries installed extensions in a target location

        Args:
            location (str): target location
        Returns:
            [str]: list of names of installed packages
        """
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

    def installed(
            self,
            sender: 'ExtensionSource',
            identifier: str,  # pylint: disable=unused-argument
            location
    ) -> [Extension]:
        """
        Creates list of Extensions contained in target location

        Args:
            sender (ExtensionSource): source querying installed extensions
            identifier (str): unused argument, has to be present for structural
                typing
            location (str): location in which to search for extension
        Returns:
            [Extension]: list of extensions at location
        """
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
    def _install_extension(identifier: str, location: str, extension_name: str):
        """
        Installs extension via pip command
        Args:
            identifier(str): uri of package
            location(str): location of package
            extension_name(str): name of extension
        """
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

    def load(self, extension: Extension) -> Any:
        """
        Installs extension and loads it after installation

        Args:
            extension (Extension): extension to load
        Returns:
            module (Any): imported extension
        Raises:
            Exception: if import of module fails
        """
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
