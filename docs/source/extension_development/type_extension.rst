.. _develop_type_extension:

Develop a Type Extension
========================
Developing a :ref:`Type extension <type_extension>` is relatively simple. In this walk-through we develop a `Type` and a custom `View` for it.

.. note::

   This walk-through re-implements the `File` type already provided by the `Base` extension. The upstream source code can be found in `extensions/base`.

Defining the Extension Entrypoint
"""""""""""""""""""""""""""""""""
A valid extension is required to provide an entrypoint. Currently this means that the extension must provide two special functions called `create_extension` and `destroy_extension`. These functions are called when the extension is loaded and unloaded respectively. It is further required that these functions can be imported from the extension's root module.

We will start by creating a file called `__init__.py` in the root of our extension. This file will contain the two special functions.

.. code-block:: python
    :linenos:

    def create_extension(extension_api: ExtensionApi):
        # TODO: register the `File` type
        # TODO: register a view for the `File` type

    def destroy_extension(extension_api: ExtensionApi):
        # TODO: deregister the `File` type
        # TODO: deregister a view for the `File` type

As you can see, these methods have the `extension_api` as an argument. We can use it to register our type into the :ref:`type registry <definition_type_registry>`. Through the type registry it is then possible for BlackFennec to use our created type during :ref:`interpretation <definition_selection_process>`.


.. _type_definition:

Creating and Loading a Type Definition
""""""""""""""""""""""""""""""""""""""
The first file that needs to be created is the `Type` definition file. This file is a JSON file that contains the definition of the `Type`. The file should be named `<type_name>.json`. In the case of a `File` type it could look like this:

.. code-block:: json

    {
        "super": { "$ref": "bftype://Map" },
        "type": "File",
        "required": [
            "file_path",
            "file_type"
        ],
        "properties": {
            "file_path": {
                "super": null,
                "type": "String"
            },
            "file_type": {
                "super": null,
                "type": "String"
            }
        }
    }

The `Type` definition file contains the following information:

* The super class of the `Type`. This is the `Type` that the `Type` extends. In this case the `File` `Type` extends the `Map` `Type`. Note, that this is a reference with the `bftype://` protocol. This is a reference to a `Type` that must already be loaded in the `TypeRegistry`.
* The name of the `Type`. This is the name that will be used to reference the `Type`. In this case the `Type` is called `File`.
* Required properties. These are the properties that are required to be set on the `Type` instance. In this case the `file_path` and `file_type` properties are required.
* The properties themselves. These are the properties that are available on the `Type` instance. In this case the `file_path` and `file_type` properties are available.
  * The `file_path` property is a `String` `Type`.
  * The `file_type` property is a `String` `Type`.

With this we can extend our `__init__.py` file to register the `File` `Type` into the `TypeRegistry`:

.. code-block:: python

    FILE_TYPE = None

    def create_extension(extension_api: ExtensionApi):
        FILE_TYPE = extension_api.type_loader.load('file/file.json')
        # TODO: register a view for the `File` type

    def destroy_extension(extension_api: ExtensionApi):
        extension_api.type_registry.deregister_type(FILE_TYPE)
        # TODO: deregister a view for the `File` type

If we didn't want to add any special functionality for our new `Type` we could stop here.

.. _type.py:



Creating a Wrapper for the Type
"""""""""""""""""""""""""""""""
BlackFennec lacks the ability to create a concrete `Type` instance directly. Instead it is recommended to create a wrapper for the `Type` that can be used to interact with instances of it. The snipped below is an example of a `File` wrapper:


.. code-block:: python

    class File:
        """File type wrapper

        Helper class representing an instance of a 'File'.
        Can be used by other classes as a helper interact with the underlay more easily.
        """
        FILE_PATH_KEY = 'file_path'
        FILE_TYPE_KEY = 'file_type'

        def __init__(self, subject: Map = None):
            """File Constructor

            Args:
                subject (Map): underlying map interpretation to
                    which property calls are dispatched
            """
            self._subject: Map = subject or Map()
            if File.FILE_PATH_KEY not in self._subject.value:
                self._subject.add_item(File.FILE_PATH_KEY, String())
            if File.FILE_TYPE_KEY not in self._subject.value:
                self._subject.add_item(File.FILE_TYPE_KEY, String())

        @property
        def subject(self):
            return self._subject

        def _get_value(self, key):
            if key not in self.subject.value:
                return None
            return self.subject.value[key].value

        def _set_value(self, key, value):
            assert key in self.subject.value
            self.subject.value[key].value = value

        @property
        def file_path(self) -> str:
            return self._get_value(File.FILE_PATH_KEY)

        @file_path.setter
        def file_path(self, value: str):
            self._set_value(File.FILE_PATH_KEY, value)

        @property
        def file_type(self) -> str:
            return self._get_value(File.FILE_TYPE_KEY)

        @file_type.setter
        def file_type(self, value: str):
            self._set_value(File.FILE_TYPE_KEY, value)


Creating the View Model
"""""""""""""""""""""""
Next we want to create a view model.

.. note::

    We recommend using MVVM.

.. code-block:: python

    class FileViewModel:
    """View model for core type File."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        self._interpretation = interpretation
        self._file: File = File(interpretation.structure)

    @property
    def file_path(self):
        """Property for file path"""
        return self._file.file_path

    @file_path.setter
    def file_path(self, value: str):
        self._file.file_path = value

    @property
    def file_type(self):
        """Property for file type"""
        return self._file.file_type

    @file_type.setter
    def file_type(self, value: str):
        self._file.file_type = value

    def navigate(self):
        self._interpretation.navigate(self._interpretation.structure)


Creating the View
"""""""""""""""""

This file depends on how one wants to visualise the `Type`. Important is that your view is as responsive as possible, as you never know how big a presenter will show your type view. For an example please see the `FileView` in the `blackfennec_extensions_base` package located in `extensions/base/base/file`.


Writing a ViewFactory
"""""""""""""""""""""
Creating a view is a non-trivial problem. This is why BlackFennec does not create them itself. Instead you have to register a `ViewFactory` capable of creating a view for your `Type`.

Luckily creating a view for a `File` is rather simple. First, we create the view model and after we can construct the appropriate view.


.. code-block:: python

    class FileViewFactory:
    """Creator of the FileView"""

        def satisfies(self, specification: Specification) -> bool:
            """Test if this view factory can satisfy the specification

            Args:
                specification (Specification): the specification to be satisfied

            Returns:
                bool: True if the specification can be satisfied. Otherwise False.
            """
            return True

        def create(self, interpretation: Interpretation) -> FileView:
            """creates a FileView

            Args:
                interpretation (Interpretation): The overarching
                    interpretation.
                specification (Specification): The specification which can fine
                    tune the creation function.

            Returns:
                FileView
            """
            view_model = FileViewModel(interpretation)
            if interpretation.specification.is_request_for_preview:
                return FilePreview(view_model)

            return FileView(view_model)


Registering the View
""""""""""""""""""""
The last step is to register the view for the `File` `Type`. This can be done by adding the following code to the `create_extension` method:


.. code-block:: python

    FILE_TYPE = None

    def create_extension(extension_api: ExtensionApi):
        FILE_TYPE = extension_api.type_loader.load('file/file.json')
        extension_api.view_registry.register_view_factory(
            FILE_TYPE,
            Specification(),
            FileViewFactory())

    def destroy_extension(extension_api: ExtensionApi):
        extension_api.type_registry.deregister_type(FILE_TYPE)
        extension_api.view_registry.deregister_view_factory(
            FILE_TYPE,
            Specification())
