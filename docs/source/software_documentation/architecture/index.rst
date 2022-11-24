.. _Architecture:

Architecture
============
The ecosystem of Black Fennec can be divided into four components and the means by which they interact. From the architectural standpoint, Black Fennec provides the interfaces between the components and also some services to solve common problems. These interfaces and services are largely independent and allow for the high degree of cohesion and low coupling which is required to manage the complexity in this project. The following graph gives a good overview. It does not strive to be a perfect reflection of the code and its complexity but instead should serve as an entry point for new developers.

.. uml:: overview.puml

Black Fennec is a desktop application without backend integration. All code runs within a single tire. However, the project entails a fair amount of engineering challenges.


User Data
    :ref:`User data <definition_source_layer>` is the information the user is viewing/editing with Black Fennec. As such it is not part of the source code. When it's loaded from a file into Black Fennec it is deserialized into the :ref:`object model <object_model>`. The resulting structure will be interpreted by the interpretation service, visualised partially by extension provided views, and displayed by a presenter.

Extension
    :ref:`Extensions <definition_extension>` allow the addition of types, actions and presenters. The richer the ecosystem and the more types are available to the interpretation service the better the interpretation. At least that's the theory. Extensions get access to the :ref:`extension api <definition_extension_api>` via inversion of control (constructor dependency injection).

Visualisation
    :ref:`Visualisations <definition_type_view>` are the visual representation of the Structure. They play a big role in what the user sees and interacts with. They use the navigation service to communicate navigation requests to Black Fennec. They use the interpretation service to visualise :ref:`previews <definition_type_preview>` of substructures of themselves. Internally, MVVM is used to decouple view and logic. Note that this - from the point of view of Black Fennec - is an implementation detail and neither enforced nor required by extensions.

Presentation
    The presentation is the responsibility of the :ref:`presenter <presenter>`. It displays interpretations which are requested from the interpretation service. The presenter also observes the navigation service for navigation request and is responsible for acting on them.


Black Fennec
""""""""""""
When we take a closer look at the interfaces and services used by the "external" components, we can identify some concepts that can be found throughout this documentation. These are the high-level concepts which are important for a complete picture of the project. Each component is conceptually largely independent of the others. This allows us to tune their view of the system to their needs. Think of the facade pattern but towards the core and not to hide legacy code but to minimize complexity whereby development efficiency is maximised.

.. uml:: guts.puml

Structure
    The :ref:`structure <definition_overlay>` is the parsed user data. It is the foundation upon which the :ref:`interpretation <definition_interpretation>` is built and the fabric in which navigation is performed. It is represented in our :ref:`object model <object_model>` and can be further preprocessed by `composite adapters` such as :ref:`filter <filter_adapter>` and :ref:`overlay <overlay_adapter>`. The `composite adapters` allow specialised usage of the structure - including :ref:`advanced interpretation <advanced_interpretation>` - without manipulating the underlying structure (:ref:`underlay <definition_underlay>`).

Document System
    The :ref:`document system <definition_document_system>` is responsible to import a structure from sources such as files. With that it is responsible to abstract the access protocol and mime type.

Type System
    The :ref:`type system <definition_type_system>` is represented as a collection of known types that can be used to interpret the structure. They are stored in a registry. This allows runtime loading and unloading of the available types and is an important enabler of the extension infrastructure.

Interpretation
    The :ref:`interpretation service <definition_interpretation_service>` does most of the heavy lifting as it decides which types from the :ref:`type system <definition_type_system>` ought to be used to visualize a given structure. The service can be configured on a 'per request' basis with a :ref:`specification <specification>`, giving fine-tuned control to the user of the service. This service is used by both, the presenter and the visualisation, although they usually use different specifications.

Facade
    The facade is what the user sees. It hides all the complexity and ought to provide an intuitive interface for all possible interactions with the system.

Further information and more detailed descriptions of the mentioned components can be found in the :ref:`domain model <domain_model>`. If you are interested in the documentation of the source code :doc:`follow this link <../code/modules>`