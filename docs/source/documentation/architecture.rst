Architecture
============
The ecosystem of Black Fennec can be divided into four components and the means by which they interact. From the architectural standpoint, Black Fennec provides the interfaces between the components and also some services that solve common problems.

.. uml::
    
    @startuml

    skinparam rectangle {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
        roundCorner 25
    }

    skinparam rectangle<<core>> {
        roundCorner 1000
    }

    title Architecture Overview
    
    rectangle Presenter
    rectangle Visualisation
    rectangle Extension
    rectangle "User Data" as UA
    rectangle "Black Fennec" as BF <<core>>

    Presenter       -up->       BF
    UA              -->         BF
    Visualisation   -up->       BF
    Extension       -->         BF

    @enduml


Black Fennec
""""""""""""
When we take a closer look at the interfaces and services that are used by the "external" components, we can identify some concepts that we will find throughout this documentation.

.. uml::
    
    @startuml

    skinparam rectangle {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
        roundCorner 25
    }

    title Interfaces and Services



    package "Black Fennec" <<Frame>> {
        rectangle Navigation
        rectangle InterpretationService
        rectangle Structure
        rectangle "Type System" as TS

        InterpretationService     -up->           TS
        Structure       -[hidden]->     Navigation
    }


    rectangle Presenter
    rectangle Visualisation
    rectangle Extension
    rectangle "User Data" as UA

    Presenter       -up->       InterpretationService
    Navigation      -->         Presenter
    Visualisation   -up->       Navigation
    Visualisation   -up->       InterpretationService
    Extension       -->         TS
    UA              -->         Structure
    Visualisation   -->         Structure

    @enduml

Structure
    The :ref:`structure <definition_overlay>` is the parsed user data. It is the foundation upon which the interpretation is built and the fabric in which navigation is performed.

Type System
    The :ref:`type system <definition_type_system>` is a collection of known types that can be used to interpret the structure.

Navigation
    The :ref:`navigation service <definition_navigation_service>` allows components to request navigation within the structure. The service forwards the request to the relevant components, including the currently active presenter.

InterpretationService
    The :ref:`interpretation service <definition_interpretation_service>` does most of the heavy lifting as he decides which types from the type system ought to be used to visualize a given structure. This service is used by both, the presenter and the visualisation.

User Data
    :ref:`User data <definition_source_layer>` is the information the user is viewing/editing with Black Fennec. It is loaded into Black Fennec and interpreted into a structure, from where it will be interpreted and visualised.

Extension
    :ref:`Extensions <definition_extension>` allow the extension of the type system. The more available types the better the interpretation can get. At least that's the theory.

Visualisation
    :ref:`Visualisations <definition_info_view>` are the visual representation of the Structure. They play a big role in what the user sees and interacts with. They use the navigation service to communicate navigation events with Black Fennec. They use the interpretation service to visualise subcomponents of themselves.

Presenter
    The :ref:`presenter <presenter>` displays interpretations which he receives from the interpretation service. The presenter also acts on navigation request which are forwarded to him by the navigation service.

Further information and more detailed descriptions of the mentioned components can be found in the :doc:`domain_model`. If you are interested in the documentation of the source code :doc:`follow this link <code/modules>`