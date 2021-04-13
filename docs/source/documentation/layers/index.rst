.. _definition_layer:

The Layers
==========

.. toctree::
    :maxdepth: 2

    interpretation
    overlay
    underlay
    source_layer

Overview
""""""""
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
    Overlay         -down>     Underlay        : is based on
    Underlay        -down>     SourceLayer     : is deserialized from

    @enduml

Presenter
    The :ref:`presenter <definition_presenter>` is responsible for presenting the :ref:`interpretation <definition_interpretation>` to the user.

Interpretation
    The :ref:`interpretation <definition_interpretation>` is based on the :ref:`overlay <definition_overlay>` and created in the :ref:`selection process <definition_selection_process>`

Overlay
    The :ref:`overlay <definition_overlay>` is the processed :ref:`underlay <definition_underlay>`. It mainly resolves references.
    
Underlay
    The :ref:`underlay <definition_underlay>` is the deserialized :ref:`source layer <definition_source_layer>`. It consists solely of :ref:`core types <definition_core_types>`.

Source Layer
    The :ref:`source layer <definition_source_layer>` is the source of the information. Most often a JSON file.