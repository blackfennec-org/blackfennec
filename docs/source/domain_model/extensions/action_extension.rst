Action Extension
================
A action extension adds actions to existing types. It is common for type extensions to define actions for its own types. The actions will be displayed spatially close to the representation of the type. Conceptually, running an action will call a registered function and pass context including the associated object as parameter.

.. uml::

    @startuml

    package "Action Extension" {
    object Action
    }
    object Type
    object Object
    object Presenter
    object Context

    Action --> Type : registered for
    Object --> Type : is of
    Presenter --> Context : calls Action with
    Object -right-> Context : is
    Context -right-> Action : parameter for
    Presenter --> Action : shows registered
    Presenter --> Object : shows

    @enduml

Actions must be registered for their target types so that the active :doc:`presenter_extension` can display them. Iff the user clicks on the associated UI element the action is called with the context of its sender. The context includes a reference to the object on which the action has been called on. This allows the action to manipulate data or depend its control flow based on the context. 
