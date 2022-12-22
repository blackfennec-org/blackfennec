# -*- coding: utf-8 -*-
from blackfennec.type_system.interpretation.specification import Specification
from blackfennec.presentation_system.type_view_factory import TypeViewFactory
from blackfennec.type_system.type import Type


class TypeViewFactoryRegistry:
    """View_factory Registry Class

    Is a register of all known or registered view_factories.

    Attributes:
        _type_view_factories: stores internal view_factories
    """

    def __init__(self):
        """ type_view_factory_registry constructor.

        Initializes the _type_view_factories attribute with empty list
        """
        self._type_view_factories = []

    def get_factory(self, type, specification):
        for t, s, f in self._type_view_factories:
            if t == type and s == specification:
                return f
        return None

    def register_type_view_factory(
            self,
            type: Type,
            specification: Specification,
            type_view_factory: TypeViewFactory,
    ):
        """Function to register a new type_view_factory

            Args:
                type (type): type of type_view_factory
                specification (Specification): specification of
                    type_view_factory
                type_view_factory (TypeViewFactory): future element of the
                    type_view_factory list
        """
        self._type_view_factories.append(
            (type, specification, type_view_factory)
        )

    def deregister_type_view_factory(
            self,
            type: Type,
            specification: Specification,
    ):
        """Function to deregister a type_view_factory from the dictionary if its
            class matches the passed type_view_factory

        Args:
            type (type): type of type_view_factory
            specification (Specification): specification of type_view_factory

        """
        for t, s, f in self._type_view_factories:
            if t == type and s == specification:
                self._type_view_factories.remove((t, s, f))
                return
        raise AssertionError("type, specification not in registry")
