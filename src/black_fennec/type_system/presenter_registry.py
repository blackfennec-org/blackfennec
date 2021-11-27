# -*- coding: utf-8 -*-
class PresenterRegistry:
    """Presenter Registry Class

    Is a register of all registered presenters.

    Attributes:
        _presenters: stores internal presenters
    """

    def __init__(self):
        """presenter registry constructor.

        Initializes the _presenters attribute with empty list
        """
        self._presenters = []

    @property
    def presenters(self):
        """presenters getter

            Returns:
                list: of presenter
        """
        return list(self._presenters)

    def register_presenter(self, presenter):
        """Function to register a new presenter

            Args:
                presenter (Presenter): future element of the presenter registry
        """
        self._presenters.append(presenter)

    def deregister_presenter(self, presenter_type: type):
        """Function to deregister a presenter from the registry if its class
            matches the passed type

        Args:
            presenter_type (type): element in the type list

        """

        for current_presenter in self._presenters:
            if current_presenter.__class__ == presenter_type:
                self._presenters.remove(current_presenter)
