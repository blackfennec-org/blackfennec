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
        self._presenters = list()

    @property
    def presenters(self):
        """presenters getter

            Returns:
                list: of presenter
        """
        return self._presenters

    def register_presenter(self, presenter):
        """Function to register a new presenter

            Args:
                presenter (Presenter): future element of the presenter registry
        """
        self._presenters.append(presenter)

    def deregister_presenter(self, presenter):
        """Function to deregister a presenter from the registry

        Args:
            presenter (InfoBidder): element in the type list

        """
        self._presenters.remove(presenter)
