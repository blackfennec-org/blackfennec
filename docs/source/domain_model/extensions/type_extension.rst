Type Extension
==============
A type extension defines and adds a new :ref:`type <definition_type>` to the object model. For this new type to be usable it must be accessible to the user. Therefore, it is necessary for the extension to also provide three further components, namely a user interface henceforth `Info View`_ and a factory (`Info View Factory`_) that can produce them on demand, and a service that participates in the InfoView selection process henceforth the `Info Bidder`_.

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
    
    title Basic Type Extension Overview
    
    class Auctioneer {}
    note top of Auctioneer: Not part of this document

    package "TypeExtension" {
        class Type {}
        class InfoView {}
        class InfoViewFactory {}
        class Bidder {}
    
        InfoViewFactory -> InfoView  : (4) creates
        Bidder -left> Type : (2) advertises
        Type <-- InfoView : (5) displays
    }

    Auctioneer -> InfoViewFactory : (3) awards interpretation to
    Auctioneer -> Bidder : (1) consolidates with
    

    @enduml

.. _info_view:

Info View
"""""""""
This component is responsible for displaying the defined type adequately. For example if an extension defined the JPEG type the Info View would presumably render an image. For more click :ref:`here <definition_info_view>`.

.. _info_view_factory:

Info View Factory
"""""""""""""""""
This component is responsible for creating info views as described above. For more click :ref:`here <definition_info_view_factory>`

Info Bidder
"""""""""""
The bidders job is to evaluate how good - if at all - the associated type is able to represent a given data structure.
For more on Info Bidders click :ref:`here <definition_info_bidder>`
For an overview of the selection process click :ref:`here <definition_selection_process>`