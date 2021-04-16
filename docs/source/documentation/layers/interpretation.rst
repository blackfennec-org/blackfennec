Interpretation
==============
The domain concepts of interpretation service and interpretation have been created to allow flexibility in the implementation of the :ref:`selection process <definition_selection_process>` and to provide a layer of abstraction for the :ref:`presenter <definition_presenter>` towards the :ref:`info view <definition_info_view>`.

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
    class InterpretationService {}
    class Interpretation {}
    class "The Selection Process" as tsp
    class InfoViewFactory {}
    class InfoView {}
    
    InterpretationService     -left-> Presenter       : is passed to
    InterpretationService     -->     Interpretation  : creates
    InterpretationService     -->     InfoViewFactory : references
    Interpretation  -->     InfoView        : based on
    tsp             -left-> InterpretationService     : constructs an
    tsp             -->     InfoViewFactory : selects
    InfoViewFactory -->     InfoView        : creates

    Presenter       .down.> Interpretation  : has access to {}\nvia interpretation service
    

    @enduml

.. _definition_interpretation_service:

InterpretationService
'''''''''''''''''''''
The :ref:`selection process <definition_selection_process>` produces an interpretation service which in turn creates interpretations. To create an interpretation the interpretation service must create info views from info view factories. The resulting info views are included in the interpretation and are later displayed.

Interpretation services hold references to :ref:`info view factories <info_view_factory>` and know how to produce :ref:`info views <info_view>` from them. In GRASP terminology the interpretation service is the Creator for interpretations.

.. _definition_interpretation:

Interpretation
''''''''''''''
The interpretation contains the visualisation of a given structure which is largely based on InfoViews. An interpretation is what Black Fennec believes to be the best available representation of a given :ref:`structure <definition_overlay>`.