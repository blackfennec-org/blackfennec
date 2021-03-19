Interpretation
==============
To allow implementation flexibility in the :ref:`selection process <definition_selection_process>` and to provide a layer of abstraction for the :ref:`Presenter <definition_presenter>` towards the :ref:`info view <definition_info_view>` Info View the domain concept of interpretations has been created.

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
    
    title Interpretation Abstraction Overview
    
    class Presenter {}
    class Interpreter {}
    class Interpretation {}
    class "The Selection Process" as tsp
    class InfoViewFactory {}
    class InfoView {}
    
    Interpreter     -left-> Presenter       : is passed to
    Interpreter     -down-> Interpretation  : creates
    Interpreter     -up->   InfoViewFactory : references
    Interpretation  -down-> InfoView        : based on
    tsp             -left-> Interpreter     : constructs an
    tsp             -->     InfoViewFactory : selects
    InfoViewFactory -->     InfoView        : creates
    

    @enduml

.. _definition_interpretation:

Interpretation
''''''''''''''
An interpretation is what Black Fennec believes to be the best available representation of a :ref:`structure <definition_structure>` given the available :ref:`types <definition_type>`. It is what is presented to the user by the :ref:`Presenter <definition_presenter>`. It consists of at least one Info View but can potentially be constructed from an arbitrary number of them. However this implementation detail is abstracted and not of any concern to the Presenter.

Interpreter
'''''''''''
The :ref:`selection process <definition_selection_process>` produces an interpreter which in turn creates interpretations. Interpreters hold references to :ref:`info view factories <info_view_factory>` and know how to produce :ref:`info views <info_view>` from them. In GRASP terminology the interpreter is a Creator.