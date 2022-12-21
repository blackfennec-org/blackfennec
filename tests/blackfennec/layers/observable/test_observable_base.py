from blackfennec.layers.observable.observable_base import ObservableBase
from blackfennec.util.observable import Observable
from blackfennec.util.change_notification import ChangeNotification
from blackfennec_doubles.layers.observable.double_observable import ObservableLayerMock

def test_can_construct():
    assert ObservableBase(
        layer=ObservableLayerMock(),
        subject=Observable())

def test_does_append_to_history():
    hfv = ObservableLayerMock()
    subject = Observable()
    hb = ObservableBase(
        layer=hfv,
        subject=subject)
    subject._notify('changed', ChangeNotification(None, None))
    assert len(hfv.change_notifications) == 1


