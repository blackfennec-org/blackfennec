.. _definition_document_system:

Document System
================

The document system is a set of strategies that allows black fennec to be completely independent of the underlying file types. It is a set of interfaces that allow black fennec to read and write files in a generic way. The document system is also responsible for the file type detection and the file type association.

The overall interaction of the different components involved is visualized in the following diagram:

.. uml:: document_system.puml

.. _definition_document:

Document
--------

A document is a file that can be opened by black fennec. It is a set of data that can be read and written by black fennec. A document is traditionally a representation of a file. It leverages the :ref:`definition_resource_type` and :ref:`definition_mime_type` strategy patterns to load and parse arbitrary file types from arbitrary sources. A document can easily be created via the :ref:`definition_document_factory`.

.. _definition_document_factory:

Document Factory
----------------

The Document Factory is a factory that creates :ref:`definition_document` instances. It can be responsible for the resource/mime type detection and does the resource/mime type lookup in the :ref:`definition_resource_type_registry`/:ref:`definition_mime_type_registry`. These Registries are to be dependency injected upon creation of the Document Factory.


.. toctree::
    :caption: Subpages
    :maxdepth: 2

    mime_type
    resource_type
