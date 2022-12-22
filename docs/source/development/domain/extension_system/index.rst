.. _extension_system:

================
Extension System
================

Black Fennec application's capabilities and usability rely heavily on the availability of extensions. The Extension System is designed to be stable, with the goal of maintaining backward compatibility throughout the 1.x releases cycle. The Extension System is responsible for loading extensions, managing their lifecycle, and providing the extension API to extensions. The extension registry stores and organizes the extensions, and is used in part for dependency resolution. The following diagram illustrates the conceptual landscape of the extension system:


.. uml::
    
    @startuml Extension System

    hide circle
    hide members
    hide methods

    title Conceptual Extension Landscape

    skinparam class {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
    }

    package "Extension System" <<Frame>> {
        class "Extension" as e
        class "Extension Registry" as er
        class "Extension API" as ea
        class "Extension Service" as es

        e ----> e : depends on
        e --> ea : has access to
        es --> e : loads
        er --> e : contains

    }

    class "Some Extension" as se

    se --|> e

    @enduml

The components of the extension system, including the Extension, Extension Registry, Extension API, and Extension Service, are described in more detail on the linked pages.

.. toctree::
    :maxdepth: 1

    ./extension
    ./extension_api
    ./extension_service
    ./extension_registry
