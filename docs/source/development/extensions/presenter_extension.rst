.. _develop_presenter_extension:

=============================
Develop a Presenter Extension
=============================

Developing a :ref:`Presenter extension <presenter_extension>` certainly is a more advanced task than developing a :ref:`Type extensions <type_extension>` as a more detailed understanding of the system is required as for example navigations have to be handled.

As a basis for this walk-through on how to develop a :ref:`Presenter extension <presenter_extension>` we will take the default Presenter of black-fennec called the column-based-presenter. To read this section it might make sense to open the projects repository located at `here <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/tree/master/src/presentation/column_based_presenter>`_. This allows you to individually explore the code lying behind the column-based-presenter while reading through the following explanations.

.. hint:: The structure that is present in this presenter is how black-fennec recommends an extension should be structured. But as previously mentioned this is up to the developer of the extension.

We will now step by step explain the individual files contained in this extension.

<presenter_name>_extension.py
"""""""""""""""""""""""""""""

In this file the 'create_extension' and 'load_extension' functions are defined.

.. code-block:: python
    :linenos:

    def create_extension(extension_api: ExtensionApi):
        extension_api.presenter_registry.register_presenter(
            ColumnBasedPresenterViewFactory(
                extension_api.interpretation_service
            )
        )

    def destroy_extension(extension_api: ExtensionApi):
        extension_api.presenter_registry.deregister_presenter(
            # Hint: Only the Type is passed as this static-method has no access to the created instance of 'create_extension'
            ColumnBasedPresenterViewFactory
        )

As you can see the extension_api that is passed can be used to register our presenter into the presenter registry. Through the presenter registry it is then possible for black-fennec to use our created presenter to visualise data.

<presenter_name>_view_factory.py
""""""""""""""""""""""""""""""""

This file contains a simple factory used to create the presenter view model and inject it into the view. The simple factory is instantiated with all arguments that are later on required by the view model to be able to navigate and interpret information.
It is a *must* that the class, in our case the view factory, that is registered in the presenter registry contains a 'create' function that is can be executed without parameters. Otherwise, black-fennec will not be able to create the view of your extension, and it will not be usable.

.. code-block:: python
    :linenos:

    """Creator or the ColumnBasedPresenterView"""
    def __init__(self, interpretation_service):
        self._interpretation_service = interpretation_service

    def create(self, navigation_service) -> ColumnBasedPresenterView:
        """Create column based presenter view

        Returns:
            ColumnBasedPresenterView: The column based presenter view.
                Can be used as presenter in the main UI.
        """
        view_model = ColumnBasedPresenterViewModel(
            self._interpretation_service,
            navigation_service
        )
        return ColumnBasedPresenterView(view_model)

As visible in the code example above, the expected return of the create function is the view of our presenter.

<presenter_name>_view.py
""""""""""""""""""""""""

The presenter view is something, that is in the responsibility of the extension developer. He may inspire himself by looking at the code of the column-based-presenter this is an implementation-detail, and thus not relevant for this walk-through.

.. hint::
    One speciality of black-fennecs implementation of MVVM is the utility class Observable, which is a helper class to implement the Observer pattern. With the method call 'bind', which is bound via a named-parameter, that is passed a function and will respond to notify events with the event-name that corresponds to the named-parameter, to the view model which inherits of Observable.

<presenter_name>_view_model.py
""""""""""""""""""""""""""""""

The presenter that is currently active in black-fennec gets notified by a black-fennec component via the 'show' function. This function gets passed which interpretation has triggered the show event, and which part  of the :ref:`structure <definition_structure>` should now be displayed. This structure can be interpreted with the :ref:`interpretation_service <definition_interpretation_service>` in order for types beyond the core_types to be shown. It is the responsibility of the presenter of setting the navigation service on the interpretation he created. Otherwise, navigational requests that happen in the interpretation would not reach the presenter.
