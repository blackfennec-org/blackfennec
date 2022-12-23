.. _definition_type:

====
Type
====

The concept of a Type does not differ significantly in Black Fennec when compared to a standard definition as used in many other programming languages. As such we will focus on the peculiarities of our implementation here.

The type system is based on core types which map one to one with core structures, as shown in the following diagram:

.. uml:: types.puml


With the support from inheritance, the declarative syntax enables the reuse of definitions.

A type must inherit from `Type` and thus guarantees the existence of some properties like `create_instance`. Furthermore a type must be registered in the :ref:`definition_type_registry`. Otherwise it is unknown to the ecosystem, is not integrated, and thus the full potential of the type system remains unused.

Types are the link between structures and most other components, including :ref:`definition_type_view` and the :ref:`action_system`. As such they play a central role.

Types can be defined in different ways. The preferred way is by declaring it in a separate file and loading it with the :ref:`definition_type_loader`.

.. _inheritance:

Inheritance
"""""""""""
The Type System supports inheritance. This means that a type can inherit from another Type. The inheritance is transitive, meaning that a Type can inherit from a Type which inherits from another Type.

As such types are composites and subtypes of Core Types. This results in a type hierarchy, as shown in the following diagram:

.. uml:: type_system_hierarchy.puml



Example: Image Type
"""""""""""""""""""
If we wanted to improve the handling of images in Black Fennec we would problably want to add a :ref:`Type View <definition_type_view>` and allow :ref:`Actions <definition_action>` to be applied to them. The first step would be to define a Type so that images can be recognised and processed.

In this example we show how to define a type for images as seen in the json blow.

.. code-block:: json

    {
        "team_name": "Black Fennec",
        "team_logo": {
            "file_type": "image/png",
            "file_path": "path/to/image.png"
        }
    }

Since images are files and we want to be able to handle them as such we will inherit from `File`. The file type can be defined as shown below.

.. code-block:: json

    {
        "super": { "$ref": "bftype://Map"},
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

The `super` field tells us that `File` inherits form `Map` and thus is able to define properties. The `type` field tells us that this is the type definition for `File`. The `required` field tells us that `file_path` and `file_type` are required properties. The `properties` field defines the properties of the type. In this case `file_path` and `file_type` are required to be of type `String`.

Now we can define the type for images. We will inherit from `File` and only override the `file_type` property with a `pattern` and a `default` value.

.. code-block:: json

    {
        "super": { "$ref": "bftype://File"},
        "type": "Image",
        "properties": {
            "file_type": {
                "pattern": "^image/.*$",
                "default": "image/unknown"
            }
        }
    }

The `String` type allows us to define a `pattern` which allows us to define a regular expression that the value must match for a `Structure` to be recognised. 

The `default` value is used to create instances of the type.

The `TypeLoader` will read the type definition from the file and register it in the :ref:`definition_type_registry`. In that process the type hierarchy is merged which will produce the following structure.

.. code-block:: json

    {
        "super": {   },
        "type": "Image",
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
                "type": "String",
                "pattern": "^image/.*$",
                "default": "image/unknown"
            }
        }
    }


After loading the type, the :ref:`definition_type_registry` will be able to recognize the type. Notice how the type definition and the structure are loosely coupled. It is indeed possible for a single structure to be considered valid for multiple types (e.g. `File` and `Image`). It is also possible that a structure matches a type but has additional attributes that are not part of the type definition. If you are interested in the interpretation of structures, checkout the :ref:`selection process <definition_selection_process>`.
