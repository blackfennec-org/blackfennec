# -*- coding: utf-8 -*-
import logging
import importlib.metadata as metadata
from typing import Iterator

from .extension import Extension
from .extension_api import ExtensionApi
from .extension_registry import ExtensionRegistry

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ExtensionService:
    """
    Can import and list modules present in a local
        python namespace.
    """

    @staticmethod
    def load(
            api: ExtensionApi,
            registry: ExtensionRegistry):
        logger.info('Loading extensions')

        extensions = load_extensions(api)
        try_activate_extensions(extensions, registry)


def try_activate_extensions(extensions: list[Extension], registry: ExtensionRegistry):
    logger.debug('Trying to activate extensions')
    logger.debug(f'Extensions: {extensions}')
    graph = build_dependency_graph(extensions)
    order = topological_sort(graph)
    sorted_extensions = sort_extensions(extensions, order)
    try:
        activate_extensions(sorted_extensions, registry)
    except Exception as e:
        logger.error(f'Failed to load extensions')
        if sorted_extensions:
            try_activate_extensions(sorted_extensions, registry)


def activate_extensions(extensions: set[Extension], registry: ExtensionRegistry):
    logger.debug("activating extensions")
    logger.debug(f"Extensions: {extensions}")
    while extensions:
        extension = extensions.pop(0)
        logger.debug(f"activating {extension.name}")
        extension.activate()
        logger.debug(f"registering extension")
        registry.register(extension)
    logger.debug(f"activated all extensions: {extensions}")


def load_extensions(api: ExtensionApi) -> list[Extension]:
    entry_points = metadata.entry_points(group="blackfennec.extension")
    logger.debug(f"Found {len(entry_points)} entry_point")

    extensions = []
    for entry_point in entry_points:
        logger.debug(f'Found entry_point {entry_point.name}')
        module = entry_point.load()
        extension = module.create(api)
        extensions.append(extension)
    return extensions


def dependencies_satisfied(extension: Extension, registry: ExtensionRegistry):
    dependencies = extension.dependencies
    installed_extensions = registry.get_extension_names()
    return dependencies <= installed_extensions


def build_dependency_graph(extensions: Iterator[Extension]):
    graph = {}
    logger.debug("building dependency graph")
    logger.debug(f"\tExtensions: {extensions}")
    for extension in extensions:
        if extension.name not in graph:
                graph[extension.name] = []
        logger.debug(f"\tExtension: {extension.name}")
        for dependency in extension.dependencies:
            logger.debug(f"\t\tDependency: {dependency}")
            if dependency not in graph:
                graph[dependency] = []
            graph[dependency].append(extension.name)
    logger.debug(f'Graph: {graph}')
    return graph


def build_extension_map(extensions: Iterator[Extension]):
    extension_map = {}
    for extension in extensions:
        extension_map[extension.name] = extension
    logger.debug(f'Extension map: {extension_map}')
    return extension_map


def topological_sort(graph):
    count = {}
    for node in graph:
        count[node] = 0
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            count[neighbour] += 1

    ready = [node for node in graph if count[node] == 0]
    order = []
    while ready:
        logger.debug(f'count: {count}')
        logger.debug(f'Ready: {ready}')
        logger.debug(f'current order: {order}')
        node = ready.pop(-1)
        order.append(node)
        for neighbour in graph[node]:
            count[neighbour] -= 1
            if count[neighbour] == 0:
                ready.append(neighbour)
    logger.debug(f'Order: {order}')
    return order


def sort_extensions(extensions: Iterator[Extension], order: list):
    logger.debug(f"Extensions {extensions}")
    extension_map = build_extension_map(extensions)
    logger.debug(f"Extension map: {extension_map}")
    logger.debug(f"Order {order}")
    sorted_extensions = [extension_map[name] for name in order]
    logger.debug(f"Sorted: {sorted_extensions}")
    return sorted_extensions
