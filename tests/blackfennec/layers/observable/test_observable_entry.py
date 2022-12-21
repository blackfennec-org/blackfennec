from blackfennec.presentation_system.history_service import HistoryEntry


def test_can_construct():
    h = HistoryEntry(1, 2, 3)
    assert h
    assert h.structure == 1
    assert h.old == 2
    assert h.new == 3
