.. _definition_extension_development:
.. _extension_development:

=====================
Extension Development
=====================

The development of :ref:`extensions <extension>` is a vital part of the Black Fennec ecosystem as it allows developers and users to customize and extend the application with their own components and functionality. In this guide, we will cover the basics of extension development for Black Fennec, including how to create and register extensions, how to utilize the Extension API, and how to manage the lifecycle of extensions. By following these guidelines, you will be able to effectively develop and integrate extensions into the Black Fennec application.

In this documentation we will explore the framework for creating, managing, and utilizing extensions in the application. The purpose of the extension system is to allow users to easily extend and customize the Black Fennec application to meet their specific needs and requirements. This can include adding new types, type views, presenters, actions, and other components to the application.

The extension system in Black Fennec consists of several key components, including the :ref:`Extension API<extension_api>`, :ref:`Extension Service<extension_service>`, :ref:`Extension Registry<extension_registry>`, and individual :ref:`Extensions<extension>`. The Extension API is a collection of services that are made available to Extensions and provide access to various features and functionality within the application. The Extension Service is responsible for loading and managing the lifecycle of Extensions, including resolving dependencies and ensuring that Extensions are loaded in the correct order. The Extension Registry is a database of registered Extensions, which is used to store and manage the installed Extensions in the application.

To create an Extension, developers must define their Extension in a Python module and define an ``entry_point`` in the ``setup.py`` to be recognized by the Extension Service. Once an Extension is loaded, it can be activated allowing it to access the services and functionality provided by the Extension API.

An example of a minimal Extension is shown in the following text. To read this section it might make sense to open the projects repository which defines a `template for creating extensions <https://gitlab.ost.ch/blackfennec/blackfennec/-/tree/dev/extensions/template>`_. This allows you to more efficiently explore the code that is described below.

.. code-block:: python

    # my_extension.py

    from blackfennec.extension_system import Extension
    from blackfennec.extension_system import ExtensionApi

    
    class MyExtension(Extension):
        def __init__(self, api: ExtensionApi):
            super().__init__(
                name='My Extension', 
                api=api)

    def create(api: ExtensionApi) -> MyExtension:
        return MyExtension(api)

The Extension class is the base class for all Extensions and provides a number of useful methods and properties that can be used to interact with the application. The ``create`` function is used to instantiate the Extension and is called by the Extension Service when the Extension is loaded. The ``api`` parameter is an instance of the Extension API and provides access to the services and functionality provided by the application.

.. note::

    The ``create`` function must be defined in the module and must return an instance of the Extension class.

In addition to the Python module, an Extension must also define an ``entry_point`` in the ``setup.py`` file. This is used by the Extension Service to locate the Extension and load it into the application. The ``entry_point`` is defined as a ``blackfennec.extension`` in the ``setup.py`` file. For example:

.. code-block:: python

    # setup.py
    
    from setuptools import setup

    setup(
        name='my_extension',
        version='0.1.0',
        description='My Extension',
        author='My Name',
        entry_points={
            'blackfennec.extension': [
                'my_extension = my_extension'
            ]
        })


.. note::

    The ``entry_point`` must be defined as a ``blackfennec.extension`` and must point to the Python module containing the ``create`` function.

Once the Extension is defined, it can be installed into the application using the ``pip`` command. For example:

.. code-block:: bash

    $ pip install -e .

When the extension is installed in the environment in which Black Fennec is run, it will be loaded by the Extension Service and activated. The Extension Service will then call the ``create`` function to instantiate the Extension and provide it with an instance of the Extension API. The Extension can then access the services and functionality provided by the Extension API.

.. note::

    The Extension Service will only load Extensions that are installed in the environment in which Black Fennec is run.

    If you run Black Fennec with Flatpak, you must install the Extension in the Flatpak environment.

That's it! You have successfully created and installed an Extension into the Black Fennec application.


.. toctree::
    :maxdepth: 1
    :caption: Next steps:

    type_extension
    presenter_extension
