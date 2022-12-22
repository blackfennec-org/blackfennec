.. _definition_extension_development:

===================================
Extension Development Documentation
===================================

If you wonder how one can develop an extension for Black Fennec this is the right place for you. In this documentation the creation of :ref:`Type extensions <type_extension>` and :ref:`Presenter extensions <presenter_extension>` is elaborated, to enable the reader to write custom extensions with basic python knowledge.

Basic Extension Structure
"""""""""""""""""""""""""

Extensions get loaded by being present in an extension source which can point either to a local python package or a remote PyPI registry. On startup all enabled extensions get loaded. The load and unload of an extension happens by calling one of the two hook-points 'create_extension' and 'destroy_extension'. Without them being present in a module, the module will not be recognized and cannot be used.

This means that when developing an extension, the package containing the extension is required to import these two functions in its __init__.py File.

.. hint:: The __init__.py files are required to make Python treat the directories as containing packages. In this file, one can import functions or classes of the package and make them accessible on the package level.

As the only Parameter for your 'create_extension' and 'destroy_extension' functions they are passed the :ref:`extension API <definition_extension_api>` which is an object encapsulating multiple properties that might be needed to interact with black-fennec when developing an extension.

Besides the requirements for these two functions, an extension developer is completely free on how to structure his extension. At the moment extensions can only be developed with the GUI Framework GTK.

Developing a Type Extension
    If you are here to know how to develop a type extension, that integrates in the auction of the structure parts and can be used to create specialised types directly integrated in the present, you may take a look at :ref:`this section <develop_type_extension>`
Developing a Presenter Extension
    If you are here to know how to develop a presenter extension, that reorganises the column-based default presentation, you may take a look at :ref:`this section <develop_presenter_extension>`

.. hint::
    An extension can contain multiple presenters AND types at the same time.

.. toctree::
    :maxdepth: 1

    type_extension
    presenter_extension
    action_extension
