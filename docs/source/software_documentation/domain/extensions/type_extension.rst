.. _type_extension:

Type Extension
==============
A type extension defines and adds a new :ref:`type <definition_type>` to the object model. For this new type to be usable it must be accessible to the user. Therefore, it is necessary for the extension to also provide three further components, namely a user interface henceforth `Structure View`_ and a factory (`Structure View Factory`_) that can produce them on demand, and a service that participates in the InfoView selection process henceforth the `Structure Bidder`_.

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

.. _structure_view:

Structure View
""""""""""""""
This component is responsible for displaying the defined type adequately. For example if an extension defined the JPEG type the Structure View would presumably render an image. For more click :ref:`here <definition_type_view>`.

.. _structure_view_factory:

Structure View Factory
""""""""""""""""""""""
This component is responsible for creating structure views as described above. For more click :ref:`here <definition_type_view_factory>`
