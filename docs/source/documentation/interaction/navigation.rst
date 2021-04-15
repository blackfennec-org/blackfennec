Navigation
==========
An :ref:`InfoView <definition_info_view>` might not want to display the entire substructure it represents by itself. For example the :ref:`List <definition_type_list>` does not render its content in full. Instead the InfoView provides a clickable area (e.g a button) which when pressed should take the user to the sub-substructure. This process is called navigation.

.. uml::
    
    @startuml
    skinparam sequence {
        ParticipantBorderColor Black
        ParticipantBackgroundColor #EEE
        ParticipantBorderColor Black
        ArrowColor Black
        ActorBorderColor Black
        ActorBackgroundColor #EEE
        LifeLineBorderColor Black
    }

    actor User
    User -> InfoView                    : click \non preview
    InfoView -> Interpretation          : navigation request \nwith substructure
    Interpretation -> NavigationService : navigation request \nwith caller \nand sub-substructure
    NavigationService -> "Selection Process" : create interpretation service \nfor substructure
    "Selection Process" -> NavigationService : InterpretationService \nfor substructure
    NavigationService -> Presenter         : navigation request \nwith caller and interpretation service
    @enduml


.. _definition_navigation_service:

Navigation Service
""""""""""""""""""
The NavigationService provides the means to request the navigation to a structure. The NavigationService starts :ref:`the selection process <definition_selection_process>`, the result of which is then transferred to the Presenter. Besides the :ref:`InterpretationService <definition_interpretation_service>` the Presenter also gets the calling :ref:`Interpretation <definition_interpretation>` from the NavigationService. This allows the Presenter to visualise causality to the user.
