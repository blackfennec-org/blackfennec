.. _definition_mime_type:

=========
Mime Type
=========

Mime Types handle the different content types that are supported by the application. The Mime Type is an abstract concept, that has an implementation for each concrete Mime Type.

The Abstract Mime Type also has the responsibility to to determine the mime type of an arbitrary URI. It uses different approaches to achieve this, such as path endings, or mime type of http responses for the given :ref:`Resource Type <definition_resource_type>`.

As example of how different components interact, the following diagram contains the concrete implementation of the JSON Mime Type which intends to make the interactions more clear.

.. uml:: mime_type.puml

The diagram also contains the Structure Package with the Reference as a concrete implementation of the abstract class Structure. While not shown in the Diagram all Structures such as Map, List, String, etc. can be serialized and deserialized as it is required by the Liskov Principle. The Reference was chosen as an example because it is the most complex Structure that additionally contains Navigators which have to be handled specifically by the Mime Type.

.. _definition_mime_type_registry:
.. _mime_type_registry:

Mime Type Registry
""""""""""""""""""

The Mime Type Registry contains all registered Mime Types and can be used as a lookup service. Mime Types typically get registered at the start of the application and get deregistered at the end. The registry allows for Extensions to register their Mime Types.

Json Mime Type
"""""""""""""""

The Json Mime Type is the first MimeType implemented. It is used to serialize and deserialize the data to and from JSON.

Json Reference Serializer
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Reference Serializer is required by the Structure Serializer as it contains the strategy of how references for the specific mime type (here JSON) can be serialized and deserialized. Json References are specified in the form of URIs. Black Fennec can handle any :ref:`Resource Type <definition_resource_type>` and :ref:`Mime Type <definition_mime_type>` that is contained in the respective registries.

Json Reference Pointer
~~~~~~~~~~~~~~~~~~~~~~~

The JSON mime type also provides a Json Pointer Serializer which is able to serialize the part of the JSON Reference contained in the fragment. This JSON Pointer is implemented according to the IETF Specification (RFC 6901).

InMemory Mime Type
""""""""""""""""""

The InMemory mime type is used to reference already loaded types. It is essentially a mock mime type that does not serialize or deserialize anything. Currently it is imposible to save structures loaded with this mime type. 