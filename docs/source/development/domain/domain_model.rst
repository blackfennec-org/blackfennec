
.. _domain_model:

============
Domain Model
============

Our application's domain model is complex and multifaceted. It involves modeling dynamic objects in a way that is consistent and structured. We have implemented a structural type system that allows us to define and recognize the various types and relationships provided to the system.

One of the challenges we faced in building the model was the need to provide a flexible system that could accommodate the wide range of scenarios our users may encounter. To address this, we implemented the anything pattern, as described in the :ref:`definition_type` section.

Another key challenge was the need to provide an extension API that allows users to customize and add to the model as needed. This required us to carefully balance the need for structure and consistency with the need for flexibility and extensibility.

Ultimately, we believe that we have developed a domain model that offers a powerful and flexible foundation for our application. We hope that our documentation will help users understand and make the most of this complex but powerful system.

.. uml:: domain_model.puml


Extensions
==========

Extensions are a core part of Black Fennec but conceptually decoupled from the domain model through the extension api. Extensions are implemented as a set of classes which are loaded into the domain model at runtime. The extension api is a set of interfaces which extension can use to register functionality with Black Fennec.

As references for a working model, the following diagrams show the structure of the core and base extensions.

Core
~~~~
The core extension provides a UI for the :ref:`structure <definition_structure>`, some :ref:`actions <definition_action>`, as well as a :ref:`presenter <definition_presenter>`.

.. uml:: core_extension.puml

Base
~~~~
The bae extension introduces novel types such as Image and Url as well as the associated :ref:`views <definition_type_view>`.

.. uml:: base_extension.puml