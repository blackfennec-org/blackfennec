.. _definition_extension:
.. _extension:

=========
Extension
=========

Extensions allow developers to extend and customize the application with various components and functionality. Extensions can provide various types of components, including types, type views, presenters, actions, and more. Extensions interact with the system via the :ref:`Extension Api <extension_api>`.


.. _extension_lifecycle:

The :ref:`Extension System <extension_system>` in Black Fennec manages the lifecycle of extensions, which includes four states: at rest, loaded, active, and error state.

.. uml::

    @startuml Extension Lifecycle

    skinparam class {
    BackgroundColor White
    BorderColor Black
    ArrowColor Black
    }

    hide circle
    hide members
    hide methods

    left to right direction

    title Extension Lifecycle

    state "At Rest" as ar
    state "Loaded" as l
    state "Active" as a
    state "Error State" as es

    ar --> l : load
    l --> a : activate
    a --> ar : deactivate
    a --> es : error
    l --> es : error

    @enduml

When an extension is first installed, it is in the "at rest" state. When the Extension Service loads the extension, it transitions to the "loaded" state. From there, the extension can be activated and move to the "active" state, allowing it to utilize the features and functionality of the Black Fennec application. If an error occurs while the extension is active, it will transition to the "error state". In this state the extension can be reset and return to the "at rest" state.

Extensions can also define dependencies on other extensions, which means that they require certain other extensions to be installed and loaded in order to function properly. This helps to ensure that the necessary components and functionality are available to the extension.

There are also some recommended extensions that are commonly used in Black Fennec installations. These include the Black Fennec Core extension, which provides the basic type views, a presenter, and some actions, and the Black Fennec Base extension, which provides commonly used types such as dates, URLs, and images.

.. automodule:: blackfennec.extension_system.extension
    :noindex:
    :members:
    :undoc-members:
    :show-inheritance:
