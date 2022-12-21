.. _definition_source_layer:

============
Source Layer
============

The source layer represents the actual source of the data and is not a concept found in any other part of the documentation. It can be thought of as the raw, unprocessed data that is fed into the system. Currently, only JSON is officially supported as a source, but it is possible to extend the system to support other mime types such as XML or YAML. The actual implementation of the source layer is realized with the Document System, which is responsible for handling the deserialization and organization of the raw data. 
