.. _domain:

======
Domain
======

This document introduces the domain model of Black Fennec. Due to the inherit complexity of the project different levels of abstraction are used. If you are interested in how a specific component works just follow the link to its dedicated page. 

This high level abstraction only shows the most prominent components of the system. It is meant to give an overview over the core components and their interactions.


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
    The :ref:`navigation service <definition_navigation_service>` loosely binds interpretations to presenters and therefore breaks the dependency cycle we see in the simplified domain modelComing Soon™


.



The currently documented domain model is depicted below. To read more about the components take a look at the table of contents below the diagram.
