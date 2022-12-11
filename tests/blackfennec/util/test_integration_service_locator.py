import pytest
from blackfennec.util.service_locator import ServiceLocator


pytestmark = pytest.mark.integration

def test_can_construct_service_locator():
    assert ServiceLocator()
