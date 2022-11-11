from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.structure.double_structure import StructureMock

def test_create_document_registry():
    registry = DocumentRegistry()
    assert registry is not None

def test_register_document():
    registry = DocumentRegistry()
    content = Dummy()
    document = DocumentMock(content=content)
    registry.register_document(document)
    assert registry._documents[content] == document

def test_get_document():
    registry = DocumentRegistry()
    content = StructureMock()
    document = DocumentMock(content=content)
    registry.register_document(document)
    assert registry.get_document(content) == document
