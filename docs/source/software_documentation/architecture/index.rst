.. _architecture:

Architecture
============
The ecosystem of Black Fennec can be divided into four components and the means by which they interact. From the architectural standpoint, Black Fennec provides the interfaces between the components and also some services that solve common problems. These interfaces and services are largely independent and allow for the high degree of cohesion and low coupling which is required to manage the complexity of this project.

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
    
    rectangle Presentation
    rectangle Visualisation
    rectangle Extension
    rectangle "User Data" as UA
    rectangle "Black Fennec" as BF <<core>>

    Presentation       -up->       BF
    UA              -->         BF
    Visualisation   -up->       BF
    Extension       -->         BF

    @enduml

Black Fennec is a desktop application without backend integration. All code runs within a single tire. However, the project entails a fair amount of engineering challenges.


Black Fennec
""""""""""""
When we take a closer look at the interfaces and services used by the "external" components, we can identify some concepts that can be found throughout this documentation.

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
        rectangle Interpretation
        rectangle Structure
        rectangle "Type System" as TS

        Interpretation     -up->           TS
        Structure       -[hidden]->     Navigation
    }


    rectangle Presentation
    rectangle Visualisation
    rectangle Extension
    rectangle "User Data" as UA

    Presentation       -up->       Interpretation
    Navigation      -->         Presentation
    Visualisation   -up->       Navigation
    Visualisation   -up->       Interpretation
    Extension       -->         TS
    UA              -->         Structure
    Visualisation   -->         Structure

    @enduml

Structure
    The :ref:`structure <definition_overlay>` is the parsed user data. It is the foundation upon which the :ref:`interpretation <definition_interpretation>` is built and the fabric in which navigation is performed. It is represented in our :ref:`object model <object_model>` and can be further preprocessed by adapter classes such as :ref:`filter <filter_adapter>` and :ref:`overlay <overlay_adapter>`. The adapter allow specialised usage of the structure - including :ref:`advanced interpretation <advanced_interpretation>` - without manipulating the object model.

Type System
    The :ref:`type system <definition_type_system>` is represented as a collection of known types that can be used to interpret the structure. They are stored in a registry. This allows runtime loading and unloading of the available types and is an important enabler of the extension infrastructure.

Navigation
    The :ref:`navigation service <definition_navigation_service>` allows components to request navigation within the structure. The service forwards the request to the relevant components via observer pattern. Usually, the observer is set to the currently active presenter.

Interpretation
    The :ref:`interpretation service <definition_interpretation_service>` does most of the heavy lifting as it decides which types from the :ref:`type system <definition_type_system>` ought to be used to visualize a given structure. The service can be configured on a per request basis with a :ref:`specification <specification>`, giving fine tuned control to the user of the service. This service is used by both, the presenter and the visualisation, although they usually use different specifications.

User Data
    :ref:`User data <definition_source_layer>` is the information the user is viewing/editing with Black Fennec. When it loaded from a file into Black Fennec it is deserialized into the :ref:`object model <object_model>`. The resulting structure will be interpreted by the interpretation service, visualised partially by extension provided views, and displayed by a presenter.

Extension
    :ref:`Extensions <definition_extension>` allow the extension of the type system. The more available types the better the interpretation can get. At least that's the theory. Extensions get access to the :ref:`extension api <definition_extension_api>` via inversion of control e.g. dependency injection.

Visualisation
    :ref:`Visualisations <definition_info_view>` are the visual representation of the Structure. They play a big role in what the user sees and interacts with. They use the navigation service to communicate navigation requests to Black Fennec. They use the interpretation service to visualise :ref:`previews <definition_preview>` of substructures of themselves. Internally, MVVM is used to decouple view and logic. Note that this - from the point of view from Black Fennec - is an implementation detail and neither enforced nor required by extensions.

Presentation
    The presentation is the responsibility of the :ref:`presenter <presenter>`. It displays interpretations which are requested from the interpretation service. The presenter also observes the navigation service for navigation request and is responsible for acting on them.

Further information and more detailed descriptions of the mentioned components can be found in the :ref:`domain model <domain_model>`. If you are interested in the documentation of the source code :doc:`follow this link <../code/modules>`