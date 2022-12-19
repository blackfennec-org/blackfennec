.. _domain:

======
Domain
======

This section is dedicated to the domain of Black Fennec. Due to the inherit complexity of the project different levels of abstraction are used. If you are interested in a specific component follow the link to its dedicated page. 

On this page a high level overview of the domain is given. The following diagram shows the most important components of the domain model.

.. toctree::
    :maxdepth: 1
    :hidden:

    domain_model
    structure/index
    type_system/index
    document_system/index
    action_system/index
    extension_system/index
    layers/index
    presentation_system/index


.. uml:: domain_overview.puml


Structure
    The :ref:`structure <definition_structure>` is the core of the domain model. It represents the deserialized data, which can come in any from thanks to the implementation of the anything pattern.

Type System
    The :ref:`type system <definition_type_system>` is another core component of the domain model. It provides the capability to define custom types which is used by extensions to add novell types to the system. Furthermore, the :ref:`interpretation service <interpretation_service>` is responsible for evaluating a structure and determining which types it implements.

Action System
    The :ref:`action system <action_system>` is providing the needed infrastructure to define and register actions. Actions are used to define custom procedures which the user can trigger.

Presentation System
    The :ref:`presentation system <presentation_system>` is responsible for everything to do with presentation, including :ref:`presenters <definition_presenter>` and :ref:`views <definition_type_view>`.

Document System
    The :ref:`document system <definition_document_system>` is responsible for handling the serialization and deserialization of different :ref:`mime types <definition_mime_type>` from various :ref:`resource types <definition_resource_type>`.


For a more complete overview of the domain model see the :ref:`detailed domain model <domain_model>` page.
