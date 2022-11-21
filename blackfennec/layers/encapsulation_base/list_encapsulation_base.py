# -*- coding: utf-8 -*-
import logging

from blackfennec.layers.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from blackfennec.structure.list import List
from blackfennec.structure.structure import Structure
from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)


class ListEncapsulationBase(EncapsulationBase, List):
    """Base Class for ecapsulations of a List.

    Contains List specific overrides of certain functions
        to ensure the encapsulation of any Structure returned
        in order to stay in the encapsulation layer.
    """

    def __init__(
            self,
            layer: 'BaseFactoryVisitor',
            subject: List,
    ):
        List.__init__(self)
        EncapsulationBase.__init__(
            self,
            layer,
            subject
        )

    @property
    def subject(self) -> List:
        return self._subject

    @property
    def value(self):
        return [self._encapsulate(item) for item in self.subject.value]

    @value.setter
    def value(self, value):
        self.subject.value = [
            self._decapsulate(item) for item in (value or [])
        ]

    def add_item(self, item: Structure):
        """Append item to list type.

        Args:
            item (Structure): Item to append.
        """
        decapsulated_item = self._decapsulate(item)
        self.subject.add_item(decapsulated_item)

    def remove_item(self, item: Structure):
        """Remove item from List.

        Args:
            item (Structure): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        decapsulated_value = self._decapsulate(item)
        self.subject.remove_item(decapsulated_value)

    def _dispatch_change_notification(
            self,
            sender,
            notification: ChangeNotification
    ):
        encapsulated_notification = ChangeNotification(
            [self._encapsulate(item) for item in notification.old_value],
            [self._encapsulate(item) for item in notification.new_value],
        )
        super()._dispatch_change_notification(sender, encapsulated_notification)

    def __repr__(self):
        return f'ListEncapsulationBase({self.subject.__repr__()})'
