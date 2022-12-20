.. _Architecture:

============
Architecture
============

The ecosystem of Black Fennec can be divided into four components and the means by which they interact. From the architectural standpoint, Black Fennec provides the interfaces between the components and also some services to solve common problems. These interfaces and services are largely independent and allow for the high degree of cohesion and low coupling which is required to manage the complexity in this project. The following graph gives a good overview. It does not strive to be a perfect reflection of the code and its complexity but instead should serve as an entry point for new developers.

.. uml:: overview.puml

Black Fennec is a desktop application without backend integration. All code runs within a single tire. However, the project entails a fair amount of engineering challenges.


User Data
    :ref:`User data <definition_source_layer>` is the information the user is viewing/editing with Black Fennec. As such it is not part of the source code. When it's loaded from a file into Black Fennec it is deserialized into the :ref:`object model <object_model>`. The resulting structure will be interpreted through the type system, visualized partially by extension provided views, and displayed by a presenter.

Types
    :ref:`Types <definition_type>` can be added by extensions. The richer the ecosystem and the more available types the better the interpretation. At least that's the theory.

Actions
    :ref:`Actions <definition_action>` are extension defined procedures which the user can trigger. They can define preconditions in the form of a type and are able to run code and manipulate the structure.

Resource Types
    A :ref:`Resource Type <definition_resource_type>` enables access to a specific type of resource. It is registered to a protocol and provides the implementation to read and write to it. It is used by the :ref:`document system <definition_document_system>` to abstract the access to the resource.

Mime Types
    A :ref:`Mime Type <definition_mime_type>` is responsible for parsing the contents of a :ref:`Resource <definition_resource_type>` and is identified by a string. In combination it allows the :ref:`document system <definition_document_system>` to abstract the access to the resource and mitigates the combinatorial explosion of possible file formats and protocols.

Views
    :ref:`Visualisations <definition_type_view>` are the visual representation of the Structure. They play a big role in what the user sees and interacts with. Internally, MVVM is used to decouple view and logic. Note that this - from the point of view of Black Fennec - is an implementation detail and neither enforced nor required by extensions.

Presenters
    The presentation is the responsibility of the :ref:`presenter <presenter>`. It displays the interpreted structure which are requested from the :ref:`interpretation service <definition_interpretation_service>`. The presenter also observes the :ref:`navigation service <definition_navigation_service>` for navigation request and is responsible for acting on them.


Black Fennec
""""""""""""
When we take a closer look at the interfaces and services used by the "external" components, we can identify some concepts that can be found throughout this documentation. These are the high-level concepts which are important to understand the bigger picture. Each component is conceptually largely independent of the others. This allows us to tune their view of the system to their needs. Think of the facade pattern but towards the core and not to hide legacy code and ths it minimizes complexity whereby development efficiency is maximized.

.. uml:: guts.puml

Structure
    The :ref:`structure <definition_overlay>` is the parsed user data. It is the foundation upon which the :ref:`interpretation <definition_interpretation>` is built and the fabric in which navigation is performed. It is implemented in our :ref:`object model <object_model>` and can be further preprocessed by :ref:`layers <definition_layer>` such as the :ref:`overlay <overlay_adapter>`. The layers allow specialized usage of the structure - including :ref:`advanced interpretation <advanced_interpretation>` - without manipulating the underlying data (:ref:`underlay <definition_underlay>`).


Type System
    The :ref:`type system <definition_type_system>` is represented as a collection of known types that can be used to interpret the structure. They are stored in a registry. This allows runtime loading and unloading of the available types and is an important enabler of the extension infrastructure.
    The :ref:`interpretation service <definition_interpretation_service>` does most of the heavy lifting as it decides which types from the :ref:`type system <definition_type_system>` ought to be used to visualize a given structure. The service can be configured on a 'per request' basis with a :ref:`specification <specification>`, giving fine-tuned control to the user of the service.

Action System
    The :ref:`action system <definition_action_system>` is responsible to execute actions. It is the interface between the user and the :ref:`action <definition_action>` and is responsible to check the preconditions and to execute the action. It is also responsible to provide the user with a list of available actions.

Document System
    The :ref:`document system <definition_document_system>` is responsible to import a structure from sources such as files. With that it is responsible to abstract the access protocol and mime type, both of which can be loaded at runtime by extensions.

Presentation System
    The :ref:`presentation system <presentation_system>` manages the available :ref:`views <definition_type_view>` and :ref:`presenters <presenter>`. It hides all the complexity and ought to provide an intuitive interface for all possible interactions with the system.


Further information and more detailed descriptions of the mentioned components can be found in the :ref:`domain model <domain_model>`. If you are interested in the documentation of the source code :doc:`follow this link <../code/modules>`