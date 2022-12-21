.. _definition_type_view:
.. _definition_type_preview:

=====
Views
=====

The View class is a base class for all views for structures in the Black Fennec software. A view is a widget that represents the visual representation of a type within the software. It serves as a means of displaying information to the user and facilitating interaction with the software.

The ViewFactory class is a base class for all view factories in the Black Fennec software. A view factory is a class that creates views for a specific type. It has two main methods: `satisfies` and `create`. The `satisfies` method tests if the view factory can satisfy a given specification, returning a Boolean value indicating whether the specification can be satisfied. This can then be leveraged by a presenter or also another view responsible of showing child views to specify what kind of view should be created.
The `create` method creates a view based on a given interpretation, which is an overarching representation of an interpreted structure.

Together, the View and ViewFactory classes play important roles in the presentation and visualization of information within the Black Fennec software, enabling the software to display and interact with data in a flexible and extensible manner. These two classes are primarily used by the Extensions which define custom views for specific types.
