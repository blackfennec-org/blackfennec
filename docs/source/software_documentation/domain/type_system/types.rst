.. _definition_type:

Type
====
The domain concept of a type is the emerging property of the three components InfoView_ InfoViewFactory_ and InfoBidder_. Black Fennec never directly interacts with an actual object that is considered the type of a structure. However, in practice we often find type classes to be part of the implementation.

.. attention:: Info might be a synonym for Type

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
    
    package "Type" {
        class InfoView {}
        class InfoViewFactory {}
        class InfoBidder {}

        InfoViewFactory ->      InfoView    : creates
    }
    @enduml



.. _definition_info_view:

InfoView
""""""""
This component is the user interface of the "type". It provides the UI for the underlying structure and allows editing it. The InfoView will be entailed in a frame called the interpretation. The active presenter places the interpretation on the screen and defines its size. It is in the responsibility of the InfoView to utilise the given space responsively.

.. caution:: It is highly discouraged to use scrollable views in Info Views. The recommended approach is to leave overflow handling up to the Presenter.


.. _definition_preview:

InfoPreview
"""""""""""
Similar to the view, the preview provides the UI for the underlining structure. The difference between the two is the context in which they are used. The preview is used within lists and values of maps to tease the element.

.. _definition_info_view_factory:

InfoViewFactory
"""""""""""""""
The construction of an InfoView might be complicated. The information is expected to be encapsulated in a Creator [#]_. The creator must be registered via the extension api and is used by Black Fennec to instantiate Info Views when needed. The document on interpretation provides more details on this process.

.. _definition_info_bidder:

InfoBidder
""""""""""
The bidders job is to evaluate how good - if at all - the associated type is able to represent a given data structure. The result is forwarded to the auctioneer as the bid of this type. If the bid wins the auction the info view will be displayed by the active presenter.

For an overview of the selection process click :ref:`here <definition_selection_process>`

Definition of a Type
""""""""""""""""""""
The definition of a type might seem counter intuitive at first. With this example we demonstrate the thought process. It uses JSON and Python-pseudo-code.

.. code-block:: json

    {
        "team_name": "Black Fennec",
        "members": [
            {
                "first_name": "Alice",
                "last_name": "Doe"
            },
            {
                "first_name": "Bob",
                "last_name": "Doe"
            }
        ]
    }


This structure contains two cascaded types. The outer type shall be "Team" and is defined as follows:

.. code-block:: python

    def is_team(structure):
        return "team_name" in structure 
            && typeof(structure["team_name"]) == String
            && "members" in structure 
            && typeof(structure["members"]) == List 
            && structure["members"].all((member) => typeof(member) == Person))

And the inner structure is "Person" which for this example is defined as follows:

.. code-block:: python

    def is_person(structure):
        return "first_name" in structure 
            && typeof(structure["first_name"]) == String
            && "last_name" in structure 
            && typeof(structure["last_name"]) == String

.. hint:: The typeof function returns an oracle that can answer the question if the given structure can be considered to be of a certain type.


Notice how the type definition and the structure are loosely coupled. It is indeed possible for a single structure to be considered valid for multiple types. It is also possible that a structure matches a type but has additional attributes that are not part of the type definition. This could be considered a dynamic subtype. The :ref:`selection process <definition_selection_process>` is required to create an interpretation that displays all attributes.


.. [#] according to GRASP: https://en.wikipedia.org/wiki/GRASP_%28object-oriented_design%29#Creator