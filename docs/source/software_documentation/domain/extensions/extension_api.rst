.. _definition_extension_api:

Extension Api
=============
To integrate :ref:`extensions <definition_extension>` into the domain of Black Fennec, the ExtensionApi is injected at load time. This interface allows extensions to register themselves to hooks and into registries. Extensions are not treated differently, regardless of their conceptual type.

.. py:class:: ExtensionApi
    
    The Extension Api is injected into Extensions at load time.

.. py:attribute:: ExtensionApi.type_registry
    :type: TypeRegistry

    The :ref:`type registry <definition_type_registry>` is used to register types and make them known to Black Fennec.

.. py:attribute:: ExtensionApi.action_registry
    :type: ActionRegistry

.. py:attribute:: ExtensionApi.presenter_registry
    :type: PresenterRegistry

.. py:attribute:: ExtensionApi.navigation_service
    :type: NavigationService

.. py:attribute:: ExtensionApi.interpretation_service
    :type: InterpretationService
