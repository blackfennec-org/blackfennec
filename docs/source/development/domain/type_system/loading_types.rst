"""""""""""""
Loading Types
"""""""""""""


.. uml:: loading_types.puml


.. _definition_type_loader:

Type Loader
"""""""""""
The Type Loader is able to load a Type from a file. It is available through the :ref:`Extension API<definition_extension_api>` and can thus be used by extensions to define Types in a declarative way. Internally, the Type Loader uses the :ref:`Document System <definition_document_system>` to load the files, allowing the extensions to define types in any supported mime type and from any supported resource. Further it applies an :ref:`definition_overlay` such that references to other types are resolved correctly. This is used in combination with the :ref:`Black Fennec Type Resource Type<definition_bftype_resource_type>` to implement inheritance.

