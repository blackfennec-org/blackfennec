from pathlib import Path
from .type_parser import TypeParser
from blackfennec.layers.overlay.overlay import Overlay


class TypeLoader:
    def __init__(self, document_factory, type_registry):
        self._document_factory = document_factory
        self._layers = [Overlay()]
        self._type_registry = type_registry

    def _apply_layers(self, structure):
        for layer in self._layers:
            structure = layer.apply(structure)
        return structure

    def load(self, absolute_path: str):
        document = self._document_factory.create(absolute_path)
        structure = self._apply_layers(document.content)
        type = TypeParser.parse(structure)
        self._type_registry.register_type(type)
        return type
