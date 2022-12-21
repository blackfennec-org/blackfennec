from blackfennec.util.change_notification import ChangeNotification
from .observable_factory_visitor import ObservableFactoryVisitor
from blackfennec.util.observable import Observable

class ObservableLayer(Observable):
    def __init__(self):
        super().__init__()
        self._factory = ObservableFactoryVisitor(self)
        self._layer = {}

    def apply(self, structure):
        if structure in self._layer:
            return self._layer[structure]
        encap = structure.accept(self._factory)
        self._layer[structure] = encap
        return encap

    def on_changed(self, sender, notification: ChangeNotification):
        self._notify('changed', notification, sender=sender)
