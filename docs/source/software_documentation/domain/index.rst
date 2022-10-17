.. _domain_model:

Domain Model
============
This document introduces the domain model of Black Fennec. Due to the inherit complexity of the project different levels of abstraction are used. If you are interested in how a specific component works just follow the link to its dedicated page where it is described in more detail. 

Simplified Domain Model
"""""""""""""""""""""""
This high level abstraction only shows the most prominent components of the system. It is meant to give an overview over the core components and their interactions.

.. uml:: simplified_domain_model.puml

Interpretation Service
    The :ref:`selection process <definition_selection_process>` is responsible for creating interpretations based on a structure and the available types.

Structure
    :ref:`Structure <definition_overlay>` is the generic term for the data in our object model, since structure is the only universally available property of all data and is as such the only common denominator.

Types
    A :ref:`type <definition_type>` is a description of a structure. A type is always associated with exactly one specialised user interface called an structure view.

Interpretation
    The :ref:`interpretation <definition_interpretation>` is the visualisation of a given structure. It is the result of the selection process and limited by the available types.

Presenter
    The :ref:`presenter <presenter>` positions interpretations on the screen and thus presents the interpreted structure to the user.

Navigation Service
    The :ref:`navigation service <definition_navigation_service>` loosely binds interpretations to presenters and therefore breaks the dependency cycle we see in the simplified domain model.

.. _dynamic_system_views:

Open File Sequence
------------------
A typical workflow starts by opening a file. The following sequence diagram illustrates the involved modules and their interactions.

.. uml:: open_file.puml

Navigation Sequence
-------------------
User defined data is usually - depending on presenter - not shown in full to the user at once. The default presenter for example, starts by only showing the top most level of the structure. Navigation within the structure is common to access deeper level. The following sequence diagram illustrates this process.

.. uml:: navigation/navigation_sequence.puml

Interpretation Sequence
-----------------------
In the earlier diagrams the shorthand "magic" was used to describe the process of interpreting a structure. The following sequence diagram describes this process in more detail.

.. uml:: interpretation/interpretation_sequence.puml

The Domain Model
""""""""""""""""

The currently documented domain model is depicted below. To read more about the components take a look at the table of contents below the diagram.

.. uml:: domain_model.puml

.. toctree::
    :maxdepth: 3

    extensions/index
    interpretation/index
    navigation/index
    structure/index
    type_system/index
    document_system/index
    action_system/index
    facade/index
