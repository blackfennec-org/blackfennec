.. _definition_resource_type:

Resource Type
==============

Resource Types handle the different data resources that are supported by the application. The Resource Type is an abstract concept, that has an implementation for each concrete Resource Type. As example of how different components interact, the following diagram contains the concrete implementation of the Http Resource Type which makes the interactions more clear.

The Abstract Resource Type has the responsibility to determine the right resource type from an arbitrary URI. This is done via the Scheme/Protocol contained in the given URI. If not protocol can be found the fallback type 'file' is used.

As example of how different components interact, the following diagram contains the concrete implementation of the Http Resource Type which intends to make the interactions more clear.

.. uml:: resource_type.puml

.. _definition_resource_type_registry:

Resource Type Registry
"""""""""""""""""""""""

The Resource Type Registry contains all registered Resource Types and can be used as a lookup service. Resource Types typically get registered at the start of the application and get deregistered at the end. The registry allows for Extensions to register their own Resource Types.

Https Resource Type
""""""""""""""""""""

The Https Resource Type is a concrete implementation of the Abstract Resource Type. It is responsible for handling all Https requests. This allows Black Fennec to load data from remote servers in the same form as it would handle a local file.

File Resource Type
"""""""""""""""""""

The File Resource Type is a concrete implementation of the Abstract Resource Type. It is responsible for handling all file requests. This allows Black Fennec to load data from local files.

.. _definition_bftype_resource_type:

BfType Resource Type
"""""""""""""""""""""

The BfType Resource Type is a concrete implementation of the Abstract Resource Type. It is responsible for handling the `bftype://` protocol. This allows Black Fennec to reference :ref:`types<definition_type>` which are currently loaded in the :ref:`definition_type_registry`.