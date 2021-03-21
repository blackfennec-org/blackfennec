Navigation
==========
An :ref:`InfoView <definition_info_view>` might not want display the entire substructure it represents by itself. For example the :ref:`List <definition_type_list>` does not render its content in full. Instead the InfoView provides a clickable are (e.g a button) which when pressed should take the user to the sub-substructure. This process is called navigation.

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
    NavigationService -> "Selection Process" : create interpreter \nfor substructure
    "Selection Process" -> NavigationService : Interpreter \nfor substructure
    NavigationService -> Presenter         : navigation request \nwith caller and interpreter
    @enduml


Navigation Service
""""""""""""""""""
The NavigationService provides the means to request the navigation to a structure. The NavigationService starts :ref:`the selection process <definition_selection_process>`, the result of which is then transferred to the Presenter. Besides the :ref:`Interpreter <definition_interpreter>` the Presenter also gets the calling :ref:`Interpretation <definition_interpretation>` from the NavigationService. This allows the Presenter to visualise causality to the user.
