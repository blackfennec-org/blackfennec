.. _extension_registry:

==================
Extension Registry
==================

The Extension Registry is a component of the :ref:`Extension System <extension_system>` in the Black Fennec application. It stores the available :ref:`extensions <extension>`, allowing them to be accessed and utilized by other parts of the application.

.. uml::

    @startuml Extension Registry

    skinparam class {
        BackgroundColor White
        BorderColor Black
        ArrowColor Black
    }

    hide circle
    hide members
    hide methods

    left to right direction

    title Extension Registry

    package "Black Fennec" <<Frame>> {
        package "Extension System" <<Frame>> {
            class "Extension Registry" as er
            class "Extension" as e
            class "Extension Service" as es

                es --> e : loads
                er --> e : contains
                es --> er : fills
        }

    }

    @enduml

The Extension Registry is responsible for maintaining a list of all the available extensions within the application. It allows the Extension Service to load and initialize extensions, and provides a way for other parts of the application to access and utilize extensions. The Extension Registry also plays a role in dependency resolution, providing the data to ensure that extensions are loaded in the correct order.
