.. _definition_core_types:
.. _object_model:
.. _definition_structure:

=========
Structure
=========

The object model (also known as core :ref:`types <definition_type>`) defines the fundamental types. All other types are structures built with it.

The object model is a DAG - apart from references - implemented with a composite pattern. It is possible to recognise this from the member of type structure in Lists and Maps. As for References, accessing the structure they point to is a special operation and References never has any children from the perspective of the DAG. Therefore, although they can break the DAG properties this is not their default behaviour.

In combination with the composite pattern the object model also includes a visitor pattern. This visitor pattern is for various utilities such as comparison, copying and also the :ref:`layering concept <definition_layers>`.

.. uml:: structure.puml

Structure
"""""""""

Structure is the generic super class of all types in the object model. It is an abstract class and cannot be instantiated. Additionally to Structure there also exists a value structure which is the super class for all types that contain a value.

Parent of Structure
~~~~~~~~~~~~~~~~~~~
The parent of a structure is closer to the root in the :ref:`tree <definition_underlay>`.

Root of Structure
~~~~~~~~~~~~~~~~~
The root is a calculated property existing on each structure and is defined as a structure with no parent. In the :ref:`tree <definition_underlay>` it is the starting point of absolute paths.

Number
""""""
This core type represents numbers including integers and floating points.

String
""""""
This core type represents strings (e.g. "hello world"). It is also used for longer texts.

.. _definition_type_list:

List
""""
A list is a collection of structures.


Map
"""
A map is a collection of key-value pairs of structures.

.. _definition_type_reference:
.. _definition_reference:

Reference
"""""""""
A reference is an absolute or relative path to structure. This type only exists on the :ref:`underlay <definition_underlay>` and is not visible on higher :ref:`layers <definition_layer>`. The Reference consists of a list of Navigators.

.. _definition_reference_navigator:

Reference Navigation
~~~~~~~~~~~~~~~~~~~~

A Navigator is a token of the parsed Reference. The list of Navigators contained in a :ref:`reference <definition_type_reference>` are used to navigate through the :ref:`tree <definition_underlay>`.

Null
""""
Null is a special type that represents the absence of a value.

Example
"""""""

We will now look at an example of a structure. The following example is a simple structure given in the form of a JSON that represents an example person.

.. code-block:: JSON

        {
            "name": "max",
            "age": 50,
            "friends": [
                {"$ref": "#/wife"},
                "paul"
            ],
            "children": null,
            "wife": {
                "name": "eva",
                "age": 45
            }
        }

To represent this structure in the object model we would use the following code:

.. code-block:: python

        person = Map({
            'name': String('max'),
            'age': Number(50),
            'friends': List([
                Reference([RootNavigator(), ChildNavigator('wife')]),
                String('paul')
            ])
            'children': Null()
            'wife': Map({
                'name': String('eva'),
                'age': Number(45)
            })
        })
