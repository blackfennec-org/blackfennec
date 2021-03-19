Domain Model
============
.. toctree::
    :maxdepth: 2
    :caption: References

    type_system/index
    layers/index
    extensions/index
    


Simplified Domain Model
"""""""""""""""""""""""

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
    
    title Simplified Domain Model
    
    class "The Selection Process" as tsp 
    class Structure
    class Types
    class Interpretation
    class Presenter
    class Extension

    tsp             -->     Structure           : selects types for
    tsp             -->     Types               : from registered
    tsp             -->     Interpretation      : and creates
    Interpretation  -->     Presenter           : is passed to
    Extension       -up->   Types               : provides
    Extension       -right-> Presenter           : provides

    Structure   -[hidden]right->    Types
    Types       -[hidden]right->    Interpretation
    
    @enduml

The Selection Process
    The :ref:`selection process <definition_selection_process>` is responsible for creating interpretations based on a structure and the available types.

Structure
    :ref:`Structure <definition_overlay>` is the generic term for data represented in our object model.

Types
    A :ref:`type <definition_type>` describes a class of objects and commonly includes attributers. They also provide specialised user interfaces to display structures of their type.

Interpretation
    The :ref:`interpretation <interpretation>` is the result of the selection process and represents a given structure with available types.

Presenter
    The :ref:`presenter <presenter>` positions interpretations on the screen and thus presents the interpreted structure to the user.

Extensions
    :ref:`Extensions <definition_extension>` allow the addition of new functionality in the form of types and presenters to the application.