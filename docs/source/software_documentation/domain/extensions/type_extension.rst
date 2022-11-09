.. _type_extension:

Type Extension
==============
A type extension defines and adds a new `type <definition_type>` to the object model. For this new type to be usable it must be accessible to the user. Therefore, it is necessary for the extension to also provide three further components, namely a user interface henceforth `Structure View`_ and a factory (`Structure View Factory`_) that can produce them on demand, and a type definition that can participate in the selection process.

.. uml:: type_extension_overview.puml

.. _structure_view_factory:

View Factory
""""""""""""
BlackFennec does not constrain the way in which the user interface is implemented. The only requirement is that it must be able to be instantiated on demand. This is achieved by requiring the registration of a capable factory with the `ViewFactoryRegistry`. The factory is responsible for creating the widget and for providing it with the necessary dependencies.

.. _structure_view:

View
""""
A `View` for a `Type` can be defined if a custom visualisation for displaying the defined type is wanted. For example if an extension defined the JPEG type the Structure View would presumably render an image. For more click `here <definition_type_view>`.

Keep in mind that you must register your `View` via a `ViewFactory <structure_view_factory>`_ with the `ViewFactoryRegistry`.


.. _structure_action

Action
""""""
Coming Soon™