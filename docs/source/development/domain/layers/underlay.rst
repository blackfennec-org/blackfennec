.. _definition_underlay:

========
Underlay
========

Underlay is a synonym for :ref:`Structure <definition_structure>` and is the deserialized data from the :ref:`source <definition_source_layer>`. As such it is the content of a :ref:`Document <definition_document>` as created by the :ref:`Document Factory <definition_document_factory>`.

This virtual layer is closest to the :ref:`source <definition_source_layer>` and has not been modified by any :ref:`layer <definition_layer>`. However, it is possible that the :ref:`Document System <definition_document_system>` has modified the :ref:`source <definition_source_layer>` in order to create the :ref:`underlay <definition_underlay>`. These modifications are not visible to Black Fennec and will most likely be lost when the data is saved.
