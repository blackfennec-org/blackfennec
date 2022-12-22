# -*- coding: utf-8 -*-
import logging
import importlib.metadata as metadata
from typing import Iterator

from .extension import Extension
from .extension_api import ExtensionApi
from .extension_registry import ExtensionRegistry

logger = logging.getLogger(__name__)


class ExtensionService:
    @classmethod
    def load(cls,
            api: ExtensionApi,
            registry: ExtensionRegistry):
        
        extensions = cls._load_extensions(api)
        cls._register_extensions(registry, extensions)
        cls._activate_extensions(extensions)


    @classmethod
    def _load_extensions(cls, api: ExtensionApi) -> list[Extension]:
        entry_points = metadata.entry_points(group='blackfennec.extension')
        logger.debug(f'Found {len(entry_points)} entry_point')

        extensions = []
        for entry_point in entry_points:
            logger.debug(f'Found entry_point {entry_point.name}')
            module = entry_point.load()
            extension = module.create(api)
            extensions.append(extension)
        return extensions

    @classmethod
    def _register_extensions(cls, registry: ExtensionRegistry, extensions: list[Extension]):
        for extension in extensions:
            registry.register(extension)

    @classmethod
    def _activate_extensions(cls, extensions: list[Extension]):
        graph = cls._build_dependency_graph(extensions)
        count = {}
        for extension in graph:
            count[extension] = 0
        for extension, neighbours in graph.items():
            for neighbour in neighbours:
                count[neighbour] += 1

        ready = [node for node in graph if count[node] == 0]
        while ready:
            extension = ready.pop(-1)

            if not cls._try_activate_extension(extension):
                extension.state = Extension.State.FAILED
                continue

            for neighbour in graph[extension]:
                count[neighbour] -= 1
                if count[neighbour] == 0:
                    ready.append(neighbour)

        for extension in count.keys():
            if count[extension] != 0:
                extension.state = Extension.State.DEPENDENCY_MISSING

    @classmethod
    def _build_dependency_graph(cls, extensions: Iterator[Extension]):
        extensions.append(Extension('MissingDependency', None, {'MissingDependency'}))
        map = cls._build_extension_map(extensions)
        graph = {}
        for extension in extensions:
            graph[extension] = []

        for extension in extensions:
            dependencies = cls._resolve_dependencies(extension, map)
            for dependency in dependencies:
                graph[dependency].append(extension)
        return graph

    @classmethod
    def _build_extension_map(cls, extensions: Iterator[Extension]):
        extension_map = {}
        for extension in extensions:
            extension_map[extension.name] = extension
        logger.debug(f'Extension map: {extension_map}')
        return extension_map

    
    @classmethod
    def _resolve_dependencies(cls, extension: Extension, extension_map: dict[str, Extension]):
        dependencies = set()
        for dependency in extension.dependencies:
            if dependency in extension_map:
                extension = extension_map[dependency]
            else:
                extension = extension_map['MissingDependency']
            dependencies.add(extension)
        return dependencies

    @classmethod
    def _try_activate_extension(cls, extension: Extension):
        try:
            extension.activate()
            extension.state = Extension.State.ACTIVE
            return True
        except Exception as e:
            logger.error(f'Failed to activate extension {extension.name}')
            logger.error(e)
            return False
