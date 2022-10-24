from blackfennec.util.initialisation_service import InitialisationService


def test_can_construct_initialisation_service(tmp_path):
    extensions = tmp_path / "extensions.json"
    extensions.write_text("[]")
    initialisation_service = InitialisationService(extensions.as_posix())
    assert isinstance(initialisation_service, InitialisationService)
