.. _definition_structure:

The Structure
=============

.. toctree::
    :maxdepth: 2

    object_model/index
    template
    filter
    overlay
    underlay
    source_layer


.. _definition_layer:

Overview
""""""""
Although not represented in the source code itself, it is helpful to reason about the different levels of structure as layers. In this model each layer adds (or removes) something to the layer below. Services tend to act on the same layer. However this is most often because they are not aware of this concept. Layers above the underlay must be transparent which allows - in theory - arbitrary combinations to create novel layers. In practice the depicted stack is used most often. It is worth noting, that the underlay itself is not represented in code either but in fact is just the not yet processed deserialized user data represented in the :ref:`object model <object_model>`

.. uml::
    
    @startuml

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
    
    Presenter       .down>     Interpretation  : shows
    Interpretation  -down>     Overlay         : of
    Overlay         -down>     Underlay        : is adapted from
    Underlay        -down>     SourceLayer     : is deserialized from

    @enduml

Presenter
    The :ref:`presenter <definition_presenter>` is responsible for presenting the :ref:`interpretation <definition_interpretation>` to the user.

Interpretation
    The :ref:`interpretation <definition_interpretation>` is based on the :ref:`overlay <definition_overlay>` and created by the :ref:`interpretation service <interpretation_service>`

Overlay
    The :ref:`overlay <definition_overlay>` is the processed :ref:`underlay <definition_underlay>`. Its main contribution is the resolution of references.
    
Underlay
    The :ref:`underlay <definition_underlay>` is the deserialized :ref:`source layer <definition_source_layer>`. It consists solely of :ref:`core types <definition_core_types>`.

Source Layer
    The :ref:`source layer <definition_source_layer>` is the source of the information. Most often a JSON file.