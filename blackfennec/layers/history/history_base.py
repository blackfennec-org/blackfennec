# -*- coding: utf-8 -*-

from blackfennec.layers.encapsulation_base.encapsulation_base import EncapsulationBase
from blackfennec.structure.structure import Structure
from .history_entry import HistoryEntry
from blackfennec.util.change_notification import ChangeNotification


class HistoryBase(EncapsulationBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._subject.bind(changed=self._on_value_change)

    def _on_value_change(self, sender, notification: ChangeNotification):
        entry = HistoryEntry(sender, 
            notification.old_value,
            notification.new_value)
        self._layer.history.append(entry)

    @staticmethod
    def _decapsulate(item: Structure):
        decapsulated_value = item
        if isinstance(item, HistoryBase):
            factory_base: HistoryBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
