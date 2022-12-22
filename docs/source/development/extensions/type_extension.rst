.. _develop_type_extension:

========================
Develop a Type Extension
========================

A type extension defines and adds a new `type <definition_type>` to the object model. For this new type to be usable it must be accessible to the user. Therefore, it is sensible for the extension to also provide three further components, namely a user interface  :ref:`Type View <type_view>` and a factory (:ref:`Type View Factory <type_view_factory>`) that can produce them on demand, and optionally some :ref:`Actions <definition_action>`.

.. uml:: type_extension_overview.puml

Developing a type extension is relatively simple. In this walk-through we develop a :ref:`Type <definition_type>`, a custom `Type View <type_view>` and an `Action <definition_action>` for it.

.. note::

   This walk-through re-implements the ``File`` type already provided by the ``Base`` extension. The upstream source code can be found in ``extensions/base``.

Defining the Extension Entrypoint
"""""""""""""""""""""""""""""""""
A valid extension is required to provide an entrypoint. Currently this means that the extension must provide a special functions called ``create`` which takes a single parameter of type :ref:`Extension Api <extension_api>`. This function is called when the extension is :ref:`loaded <extension_lifecycle>`.

For more information on how to create the entrypoint, see the documentation on :ref:`Extension Development <extension_development>`.


Creating and Loading a Type Definition
""""""""""""""""""""""""""""""""""""""
The first file that needs to be created is the Type definition file. This file is a JSON file that contains the definition of the Type and should be named ``<type_name>.json``. In the case of a ``File`` type it could look like this:

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

The Type definition file contains the following information:

* The super class of the Type. This is the Type that our Type extends. In this case the File Type extends the :ref:`Map Type <definition_type>`. Note, that this is a reference with the ``bftype://`` protocol. This is a reference to a Type that must already be loaded in the :ref:`Type Registry <type_registry>`.
* The name of the Type. This is the name that will be used to reference the Type. In this case the Type is called ``File``.
* Required properties. These are the properties that are required to be set on instances of this type. In this case the ``file_path`` and ``file_type`` properties are required.
* The properties themselves. These are the properties that are available on the type instance. In this case the ``file_path`` and ``file_type`` properties are available.
    
    * The ``file_path`` property is a ``String`` Type.
    * The ``file_type`` property is a ``String`` Type.

With this we can extend our Extension to register the File Type into the Type Registry:

.. code-block:: python


    from blackfennec.extension_system import Extension
    from blackfennec.extension_system import ExtensionApi


    class MyExtension(Extension):
        def __init__(self, api: ExtensionApi):
            super().__init__(
                name='My Extension', 
                api=api)
            
            self._file_type = None
            self._action = None

        def register_types(self):
            # currently the type loader does also register the type
            self._file_type = self._api.type_loader.load('file/file.json')

        def deregister_types(self):
            self._api.type_registry.deregister_type(self._file_type)
            self._file_type = None

If we didn't want to add any special functionality for our new Type we could stop here.


Creating a Wrapper for the Type
"""""""""""""""""""""""""""""""
Black Fennec lacks the ability to create a concrete Type instance directly. Instead it is recommended to create a wrapper for the Type that can be used to interact with instances of it. The snipped below is an example of a File wrapper:


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

This file depends on how one wants to visualize the Type. Important is that your view is as responsive as possible, as you never know how big a presenter will show your type view. For an example please see the `FileView` in the ``Base Extension`` package located in ``extensions/base/base/file``.


Writing a ViewFactory
"""""""""""""""""""""
Creating a view is a non-trivial problem. This is why Black Fennec does not create them itself. Instead you have to register a `ViewFactory` capable of creating a view for your Type.

Luckily creating a view for a File is rather simple. First, we create the view model and after we can construct the appropriate view.


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

    class MyExtension(Extension):
        # ...

        def register_view_factories(self):
            self._api.view_registry.register_view_factory(
                self._file_type,
                Specification(),
                FileViewFactory())

        def deregister_view_factories(self):
            self._api.view_registry.deregister_type_view_factory(
                self._file_type,
                Specification())


Creating an Action
""""""""""""""""""
An :ref:`Action <definition_action>` always registers itself to a Type. In return we are guaranteed to receive an instance of this type when the action is triggered. We will register our action to the File type.

The definition of an action is again relatively simple. We only need to implement a method called ``execute`` and two properties describing the action.

.. code-block:: python

    from blackfennec.action_system.action import Action
    from blackfennec.action_system.context import Context

    class GuessMimeTypeAction(Action):
        def __init__(self, 
                map_type, 
                resource_type_registry: ResourceTypeRegistry):
            super().__init__(map_type)
            self._resource_type_registry: ResourceTypeRegistry = \
                resource_type_registry

        def execute(self, context: Context):
            file_type = File(context.structure)
            
            resource_type_id = ResourceType.try_determine_resource_type(
                file_type.file_path)
            
            resource_type = self._resource_type_registry.resource_types[
                resource_type_id
            ]

            mime_type = MimeType.try_determine_mime_type(
                file_type.file_path,

                resource_type)
            file_type.file_type = mime_type

        @property
        def name(self):
            return "guess mime type"

        @property
        def description(self):
            return """Tries to determine the mime type of a file."""


The ``execute`` method is called when the action is triggered. The ``context`` parameter contains the instance of the type the action is registered to but we have to "cast" it with our wrapper. In our case this is a ``File`` instance. We can use this instance to access the file path and to set the mime type.

Finally, we need to register the action to the ``File`` type. This is done in the ``register_actions`` method.

.. code-block:: python

    class MyExtension(Extension):
        # ...

        def register_actions(self):
            self._action = DetectMimeTypeAction(self._file_type)
            self._api.action_registry.register_action(self._action)

        def deregister_actions(self):
            self._api.action_registry.deregister_action(self._action)
            self._action = None

Conclusion
""""""""""
In conclusion, the Black Fennec extension system allows developers to easily add custom functionality to the application through the creation of type extensions. By following the steps outlined in this tutorial, developers can create a new type, create a custom user interface for that type, and add actions to manipulate instances of that type. The extension system provides a clear and intuitive way to extend Black Fennec and tailor it to specific needs and use cases.
