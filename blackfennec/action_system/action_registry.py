# -*- coding: utf-8 -*-
from blackfennec.type_system.type import Type
from .action import Action


class ActionRegistry:
    def __init__(self):
        self._actions: dict[Type, list[Action]] = {}

    @property
    def actions(self) -> dict[Type, list[Action]]:
        return dict(self._actions)

    def get_actions(self, type: Type) -> list[Action]:
        """Function to get all actions for a specific type"""
        if type not in self._actions:
            return []
        return self._actions[type]
    
    def register_action(self, action: Action) -> None:
        """Function to register a new action"""
        if action.type not in self._actions:
            self._actions[action.type] = []
        self._actions[action.type].append(action)

    def deregister_action(self, action: Action) -> None:
        """Function to deregister an action"""
        if action.type not in self._actions or \
                action not in self._actions[action.type]:
            raise AssertionError("type not in registry")
        self._actions[action.type].remove(action)
