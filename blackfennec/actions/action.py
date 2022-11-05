from abc import ABCMeta, abstractmethod, abstractproperty
from .context import Context
from blackfennec.type_system.type import Type

class Action(metaclass=ABCMeta):
    """Action Interface

    This is the interface for all actions.

    Attributes:
        type: type which is used to identify the action
    """
    def __init__(self, type: Type):
        self.type = type

    @abstractmethod
    def execute(self, context: Context) -> None:
        """Function to execute the action

        Args:
            context (Context): context of the action

        """
        ...

    @abstractproperty
    def name(self) -> str:
        """A short, identifying name for the action."""
        ...

    @abstractproperty
    def description(self) -> str:
        """An informative description of the action."""
        ...