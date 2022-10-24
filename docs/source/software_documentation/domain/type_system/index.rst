.. _definition_type_system:

Type System
===========

The type system is a set of classes which describe black fennec core types as well as novel types from blackfennec.extensions, plus a set of services for handling types. 

.. uml:: type_system.puml




.. _definition_type_loader:

Type Loader
"""""""""""
The type loader is able to load a type from a file. It is available through the :ref:`definition_extension_api` and can thus be used by extensions to define types in a declarative way. Internally, the type loader uses the :ref:`definition_document_system` to load the files, allowing the extensions to define types in any supported mime type and from any supported resource. Further it applies an :ref:`definition_overlay` such that references to other types are resolved correctly. This is used in combination with the :ref:`definition_bftype_resource_type` to implement inheritance.


.. _definition_type_registry:

Type Registry
"""""""""""""
The Type Registry is a register of all known (aka registered) :ref:`types <definition_type>`. Types which are not known to the type registry cannot be considered in the :ref:`selection process <definition_selection_process>`. The type registry is accessible to extensions via :ref:`ExtensionApi <definition_extension_api>`.


.. toctree::
    :maxdepth: 2
    :caption: References

    type