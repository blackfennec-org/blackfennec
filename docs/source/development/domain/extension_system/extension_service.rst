.. _extension_service:

"""""""""""""""""
Extension Service
"""""""""""""""""

The Extension Service is an important component of the Extension System responsible for loading and initializing extensions, and ensuring that they are properly integrated into the application.

.. uml::

    @startuml Extension Service

    skinparam class {
        BackgroundColor White
        BorderColor Black
        ArrowColor Black
    }

    hide circle
    hide members
    hide methods

    left to right direction

    title Extension Service

    package "Black Fennec" <<Frame>> {
        package "Extension System" <<Frame>> {
            class "Extension Service" as es
            class "Extension" as e
            class "Extension Registry" as er

            es --> e : loads
            er --> e : contains
            es --> er : fills
        }

    }

    @enduml

In order to load extensions, the Extension Service uses Python entry points to search for and locate extensions within the environment. It then resolves the dependency tree and defines the order in which the extensions should be loaded. Once the extensions are loaded, the Extension Service registers them in the :ref:`Extension Registry <extension_registry>`, making them available to be accessed and utilized by other parts of the application. The Extension Service plays a crucial role in ensuring that the Extension System is functioning properly and that extensions are able to interact with and utilize the features and functionality of the Black Fennec application.
