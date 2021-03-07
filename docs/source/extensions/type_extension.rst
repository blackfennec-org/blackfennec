Type Extension
==============

A type extension defines and adds a new type to the object model. For this new type to be usable it must be accessible to the user, visibly. Therefore, it is necessary for the extension to also provide three further components, namely a user interface henceforth InfoView_ and a factory that can produce them on demand, and a service that participates in the InfoView selection process henceforth the Bidder_.

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


InfoView
""""""""
This component is responsible for displaying the newly defined type adequately. For example if an extension defined the JPEG type the InfoView would presumably render the image.

Info View Factory
"""""""""""""""""
The construction of an InfoView might be complicated. The information is expected to be encapsulated in a Creator [#]_.

Bidder
""""""
For an overview of the selection process see :doc:`/type_system/selection_process`

The bidders job is to evaluate how good if at all the associated type is able to represent a given data structure. The result is forwarded to the auctioneer as the bid of this type. If the bid wins the auction it is to be expected that the InfoView will be visualised in due time.

.. [#] according to GRASP: https://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29#Creator