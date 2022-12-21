.. _definition_layers:
.. _definition_layer:

======
Layers
======

The different levels of abstraction in this model can be thought of as layers. Each layer adds (or removes) something to the layer below it. Services typically exist in a single layer, as they are not typically aware of the concept of layers. The layers above the underlay should be transparent, which allows for arbitrary combinations to be adapted to different use cases.


.. uml::
    
    @startuml

    'left to right direction

    hide circle
    hide members
    hide methods

    skinparam class {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
    }
    
    title Layers Overview
    
    class Presenter {}
    class Interpretation {}
    class Overlay {}
    class Underlay {}
    class SourceLayer
    
    Presenter       .>     Interpretation  : shows
    Interpretation  ->     Overlay         : of
    Overlay         ->     Underlay        : is adapted from
    Underlay        ->     SourceLayer     : is deserialized from

    @enduml


Presenter
    The :ref:`Presenter <definition_presenter>` is responsible for presenting the data to the user in a meaningful way. It uses the :ref:`Interpretation <definition_interpretation>` and uses it to create :ref:`Views <definition_type_view>` which it display to the user. This may involve  adding additional context or information, or interacting with the user in some way.

Interpretation
    The :ref:`Interpretation <definition_interpretation>` represents the data in a form that is easier for the Presenter to understand. It is created by the :ref:`Interpretation Service <interpretation_service>`, which processes the data and returns matching :ref:`Types <definition_type>`

Overlay
    The :ref:`Overlay <definition_overlay>` is the processed :ref:`Underlay <definition_underlay>`. It is responsible for resolving references within the data, which allows the data to be connected and linked together in a meaningful way. This may involve resolving references to external sources, or linking related pieces of data together.

Underlay
    The :ref:`Underlay <definition_underlay>` is the deserialized :ref:`Source Layer <definition_source_layer>` in the form of a structure. It represents the raw data in a more organized form, which makes it easier for the Overlay to process and resolve references. The Underlay is the starting point for the data processing pipeline, and all subsequent layers build on top of it.

Source Layer
    The :ref:`Source Layer <definition_source_layer>` is the source of the data. It can be thought of as the raw, unprocessed data that is fed into the data processing pipeline. Currently, only JSON is officially supported as a source, but it is possible to extend the system to support other mime types such as XML or YAML. 

These layers provide a high-level overview of the data processing pipeline, but there are many other layers at play as well. For more information on all layers see the table of contents below.

.. toctree::

    observable_layer
    merged_layer
    overlay
    underlay
    source_layer