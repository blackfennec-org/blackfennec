import types

from src.black_fennec.structure.structure import Structure


class RootFactory:
    @staticmethod
    def make_root(structure: Structure, uri=None, mime_type=None):
        def root(self):
            return structure

        def uri(self):
            return uri

        def mime_type():
            return mime_type

        structure.get_root = types.MethodType(root, structure)
        structure.get_uri = types.MethodType(uri, structure)
        structure.get_mimetype = types.MethodType(mime_type, structure)
