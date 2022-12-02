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
    order_extensions = sort_extensions(extensions, order)
    try:
        activate_extensions(order_extensions, registry)
    except Exception as e:
        logger.error(f'Failed to load extensions')
        if order_extensions:
            try_activate_extensions(extensions, registry)


def activate_extensions(extensions: set[Extension], registry: ExtensionRegistry):
    while extensions:
        extension = extensions.pop(0)
        extension.activate()
        registry.register(extension)


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
    for extension in extensions:
        for dependency in extension.dependencies:
            graph.get(dependency, []).append(extension.name)
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
        logger.debug(f'Order: {order}')
        node = ready.pop(-1)
        order.append(node)
        for neighbour in graph[node]:
            count[neighbour] -= 1
            if count[neighbour] == 0:
                ready.append(neighbour)
    logger.debug(f'Order: {order}')
    return order


def sort_extensions(extensions: Iterator[Extension], order: list):
    extension_map = build_extension_map(extensions)
    return [extension_map[name] for name in order]
