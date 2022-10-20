from black_fennec import EXTENSIONS
from src.black_fennec.util.initialisation_service import InitialisationService


def test_can_construct_initialisation_service():
    initialisation_service = InitialisationService(EXTENSIONS)
    assert isinstance(initialisation_service, InitialisationService)
