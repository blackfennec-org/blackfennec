# -*- coding: utf-8 -*-

class ViewFactoryRegistry:
    """View_factory Registry Class

    Is a register of all known or registered view_factories.

    Attributes:
        _view_factories: stores internal view_factories
    """

    def __init__(self):
        """ view_factory_registry constructor.

        Initializes the _view_factories attribute with empty list
        """
        self._view_factories = []

    def get_factory(self, type, specification):
        for t, s, f in self._view_factories:
            if t == type and s == specification:
                return f
        return None

    def register_view_factory(self, type, specification, view_factory):
        """Function to register a new view_factory

            Args:
                view_factory_bidder (StructureBidder): future element of the view_factory list
        """
        self._view_factories.append((type, specification, view_factory))

    def deregister_view_factory(self, type, specification):
        """Function to deregister a view_factory from the dictionary if its class
            matches the passed view_factory

        Args:
            view_factory_bidder_view_factory (view_factory): element in the view_factory list

        """
        for t, s, f in self._view_factories:
            if t == type and s == specification:
                self._view_factories.remove((t, s, f))
                return
        raise AssertionError("type, specification not in registry")
