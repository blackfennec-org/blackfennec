# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.extension.double_extension_registry import ExtensionRegistryMock
from blackfennec_doubles.extension.double_extension import ExtensionMock
from blackfennec_doubles.double_dummy import Dummy

from blackfennec.extension.extension import Extension
from blackfennec.extension.extension_service import ExtensionService


@pytest.fixture
def registry():
    return ExtensionRegistryMock()


@pytest.fixture
def api():
    return Dummy('Api')


@pytest.fixture
def service(request):
    extensions = request.param
    class ExtensionServiceStub(ExtensionService):
        @classmethod
        def _load_extensions(cls, api):
            return extensions
    return ExtensionServiceStub


@pytest.mark.parametrize('service', [
    [ExtensionMock('a')],
    [ExtensionMock('a'), ExtensionMock('b')],
    [ExtensionMock('a'), ExtensionMock('b'), ExtensionMock('c')],
], indirect=True)
def test_can_load_extensions(service, registry, api):
    service.load(api, registry)
    extensions = registry.get_extensions()
    for extension in extensions:
        extension.assert_state()


@pytest.mark.parametrize('service', [
    [ExtensionMock('a')],
    [ExtensionMock('a'), ExtensionMock('b', {'a'})],
    [ExtensionMock('a'), ExtensionMock('b', {'a'}), ExtensionMock('c', {'b'})],
], indirect=True)
def test_can_load_extensions_with_dependencies(service, registry, api):
    service.load(api, registry)
    extensions = registry.get_extensions()
    for extension in extensions:
        extension.assert_state()


@pytest.mark.parametrize('service', [
    [ExtensionMock('a', {'b'}, expected_state=Extension.State.DEPENDENCY_MISSING)],
    [ExtensionMock('a'), ExtensionMock('b', {'c'}, expected_state=Extension.State.DEPENDENCY_MISSING)],
    [ExtensionMock('a'), ExtensionMock('b', {'c'}, expected_state=Extension.State.DEPENDENCY_MISSING), ExtensionMock('c', {'d'}, expected_state=Extension.State.DEPENDENCY_MISSING)],
], indirect=True)
def test_can_load_extensions_with_missing_dependencies(service, registry, api):
    service.load(api, registry)
    extensions = registry.get_extensions()
    for extension in extensions:
        extension.assert_state()


@pytest.mark.parametrize('service', [
    [ExtensionMock('a', expected_state=Extension.State.FAILED)],
    [ExtensionMock('a', expected_state=Extension.State.FAILED), ExtensionMock('b', {'a'}, expected_state=Extension.State.DEPENDENCY_MISSING)],
    [ExtensionMock('a'), ExtensionMock('b', {'a'}, expected_state=Extension.State.FAILED), ExtensionMock('c', {'b'}, expected_state=Extension.State.DEPENDENCY_MISSING)],
], indirect=True)
def test_can_load_extensions_with_failing_extensions(service, registry, api):
    service.load(api, registry)
    extensions = registry.get_extensions()
    for extension in extensions:
        extension.assert_state()


@pytest.mark.parametrize('service', [
    [ExtensionMock('a'), ExtensionMock('b'), ExtensionMock('c', {'a', 'b'})],
    [ExtensionMock('a'), ExtensionMock('b'), ExtensionMock('c', {'a', 'b'}), ExtensionMock('d', {'c'})],
], indirect=True)
def test_can_load_extensions_with_complex_dependencies(service, registry, api):
    service.load(api, registry)
    extensions = registry.get_extensions()
    for extension in extensions:
        extension.assert_state()
