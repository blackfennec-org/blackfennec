.. _definition_type_view:
.. _definition_type_preview:
.. _type_view:

=========
Type View
=========

The view is a base class for all views for structures in the Black Fennec software. A view is a widget that represents the visual representation of a type within the software. It serves as a means of displaying information to the user and facilitating interaction with the software.

Together, the type views and type view factories play important roles in the presentation and visualization of information within the Black Fennec software, enabling the software to display and interact with data in a flexible and extensible manner. These two classes are primarily used by the Extensions which define custom views for specific :ref:`types <definition_type>`.


.. _type_view_factory:

Type View Factory
"""""""""""""""""

The type view factory class is a base class for all view factories in the Black Fennec software. A view factory is a class that creates views for a specific type. It has two main methods: `satisfies` and `create`. The `satisfies` method tests if the view factory can satisfy a given specification, returning a boolean value indicating whether the specification can be satisfied. This can then be leveraged by a presenter or also another view responsible of showing child views to specify what kind of view should be created.
The `create` method creates a view based on a given interpretation, which is an overarching representation of an interpreted structure.

.. _type_view_factory_registry:

Type View Factory Registry
""""""""""""""""""""""""""

The Type view factory registry is a central registry for all type view factories in the Black Fennec software. It serves as a point of connection between extensions that provide view factories and the various components of the software that require them. Extension developers can register their view factories with the registry, making them available for use by the software, while the software can retrieve type view factories from the registry as needed.

The type view factories contained are registered bound together with their type and also a specification that defines the use and capabilities of the type view.

Structure View Factory
""""""""""""""""""""""

The structure view factory is a more general view factory that is not specialized on a specific :ref:`type <definition_type>` and creates views for all :ref:`interpretations <interpretation>` of a structure. Thus it has the responsibility to iterate over an :ref:`interpretation <interpretation>` and create type views with the help of the type view factory for all interpreted :ref:`types <definition_type>`. It is used by a :ref:`Presenter <presenter>` to create a view for a `structure <definition_structure>`.
