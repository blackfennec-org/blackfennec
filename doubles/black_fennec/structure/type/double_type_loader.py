
from src.black_fennec.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor


class TypeLoaderMock:
    def __init__(self, type_registry):
        self._type_registry = type_registry

    def load(self, uri):
        self._type_registry.register_type(uri)
        return uri