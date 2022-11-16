from blackfennec.layers.history.history_base import HistoryBase
from blackfennec.util.observable import Observable
from blackfennec.util.change_notification import ChangeNotification
from blackfennec_doubles.layers.history.double_history_factory_visitor import HistoryFactoryVisitorMock


def test_can_construct():
    assert HistoryBase(
        visitor=None,
        subject=Observable())

def test_does_append_to_history():
    hfv = HistoryFactoryVisitorMock()
    subject = Observable()
    hb = HistoryBase(
        visitor=hfv,
        subject=subject)
    subject._notify('changed', ChangeNotification(None, None))
    assert len(hfv.history.history) == 1


