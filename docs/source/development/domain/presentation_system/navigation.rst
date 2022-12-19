==========
Navigation
==========

An :ref:`InfoView <definition_type_view>` might not want to display the entire structure it represents by itself. For example the :ref:`List <definition_type_list>` does not render its content in full. Instead the InfoView provides a clickable area (e.g a button) which when pressed should take the user to the substructure. This process is called navigation.

.. uml:: navigation_sequence.puml

.. _definition_navigation_service:

Navigation Service
""""""""""""""""""
The NavigationService provides the means to request the navigation to a structure. The NavigationService forwards the request in the form of a presentation request to the :ref:`presenter`. It is the responsibility of the presenter to get an appropriate interpretation of the structure.
