.. _presentation_system:

===================
Presentation System
===================

The presentation system is a key component of the Black Fennec software, responsible for the visual representation of information within the software and facilitating user interaction with the various components of the software. It includes a range of features and components, such as the :ref:`UI Service <ui_service>`, :ref:`Navigation Service <navigation_service>`, and :ref:`History Service <history_service>`, that enable the software to effectively display and interact with data.

The :ref:`Type View <type_view>` class is a base class for all views for structures in the Black Fennec software. A view is a widget that represents the visual representation of a type within the software, serving as a means of displaying information to the user and facilitating interaction with the software.

The :ref:`Presenter <presenter>` class is responsible for rendering the content of a tab within the software, displaying the complete contents of a file and serving as a container for other components that define how these components are bound together. One specific implementation of the Presenter is the column-based presenter, which is able to show a single level of a structure in a single column and respond to navigation requests received from the structure rendered in that column.

The Navigation Service is responsible for facilitating navigation between different views and structures within the software, forwarding presentation requests in the form of structure requests to the presenter and enabling a more intuitive and seamless user experience when navigating between different views.

The :ref:`UI Service <ui_service>` serves as the interface between the various extensions and the rest of the code base, providing access to a range of predefined UI components that can be utilized to enhance the user experience and facilitate the execution of various tasks within the software. It also acts as an interface to the clipboard and toast messages, allowing the extensions to interact with these features in a seamless and intuitive manner.

The :ref:`History Service <history_service>` is responsible for maintaining a record of the user's interactions with the software, enabling the user to navigate backwards and forwards through their history of actions within the software.

In addition to the various components described above, the presentation system also includes all views and view models of the application. But these are not described in detail here, as they are not part of the domain model.

Together, these components of the presentation system work together to decouple the rest of the code base from the UI, allowing the software to be independent of the UI to some extent.

Following is a table of contents of the aforementioned components of the presentation system:

.. toctree:: 
    :maxdepth: 2

    type_view
    presenter
    navigation_service
    ui_service
    history_service
