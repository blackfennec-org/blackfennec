Domain Model
============

.. toctree::
    :maxdepth: 2

    type_system/index
    layers/index
    interaction/index
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
    :ref:`Structure <definition_overlay>` is the generic term for the data in our object model, since structure is the only universally available property of all data and is as such the only common denominator.

Types
    A :ref:`type <definition_type>` is a description of a structure. A type is always associated with exactly one specialised user interface called an info view.

Interpretation
    The :ref:`interpretation <definition_interpretation>` is the visualisation of a given structure. It is the result of the selection process and limited by the available types.

Presenter
    The :ref:`presenter <presenter>` positions interpretations on the screen and thus presents the interpreted structure to the user.

Extension
    :ref:`Extensions <definition_extension>` are installable additions and provide new functionality in the form of types and presenters.

The Domain Model
""""""""""""""""

The currently documented domain model is depicted below. To read more about the components take a look at the table of contents at the top of the page.

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

    title The Domain Model

    class "The Selection Process" as tsp 

    package Structure <<Frame>> {
        class Overlay
        class Underlay
        class SourceLayer

        Overlay         -down->     Underlay        : based on
        Underlay        -down->     SourceLayer     : deserialized from
    }
    
    package Type <<Frame>> {
        class InfoBidder
        class InfoView
        class InfoViewFactory
        
        InfoViewFactory -> InfoView : creates
        'InfoBidder .[hidden]down.> InfoViewFactory
    }

    Class TypeRegistry
    <>    register_type

    InfoBidder          --> register_type
    InfoViewFactory     --> register_type
    register_type       --> TypeRegistry            : registration

    class Interpretation
    class Interpreter
    class Presenter

    Interpreter         o-->    "1..*"  InfoViewFactory
    Interpreter         -->             Interpretation      : creates
    'Interpreter         -->            Presenter
    Interpretation      o-->    "1..*"  InfoView
    Interpretation      -->             Overlay             : of
    'Presenter           o..>    "0..*"  Interpreter
    
    package Extensions <<Frame>> {
        abstract Extension
        class TypeExtension
        class ActionExtension
        class PresenterExtension

        Extension "1" o-- "0..*" TypeExtension
        Extension "1" o-- "0..*" ActionExtension
        Extension "1" o-- "0..*" PresenterExtension

        TypeExtension       -->     Type            : provides
        PresenterExtension  -->     Presenter       : provides
    }

    class NavigationService
    Interpretation      -->     NavigationService   : navigation request
    NavigationService   -->     tsp                 : requests interpreter
    NavigationService   -->     Presenter           : forwards navigation request \nwith interpreter

    tsp                 o-->    TypeRegistry        
    tsp                 ..>     Overlay             : has indirect access to  
    tsp                 ..>     InfoBidder          : has indirect access to
    tsp                 -->     Interpreter         : creates

    @enduml