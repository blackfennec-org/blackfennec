============
Merged Layer
============

The Merged Layer is a feature that allows you to combine two :ref:`Structures <definition_structure>` into a single structure. It is different from regular layers in that it requires two input structures instead of one, and the output is a completely new structure that cannot be traced back to its original inputs. This is demonstrated in the following example:

Consider the following two structures:


.. code-block:: json
    
    {
        "example": {
            "title": "Merged Layer Example",
            "text": "In this example we will merge two structures."
        },
        "merged": {
            "rating": 5,
            "comments": [
                "This is a comment.",
                "This is another comment."
            ]
        }
    }

If we merge the example and merged objects, the resulting structure would be:

.. code-block:: json

    {
        "title": "Merged Layer Example",
        "text": "In this example we will merge two structures.",
        "rating": 5,
        "comments": [
            "This is a comment.",
            "This is another comment."
        ]
    }

It's worth noting that the Merged Layer is currently not editable, meaning that it cannot be modified after it has been created. Despite this limitation, the merged layer plays a crucial role in implementing :ref:`inheritance <inheritance>` within the :ref:`Type System <definition_type_system>` allowing the definition of a type to be merged with the definition of its super type, similar to the __proto__ property in JavaScript.


Shadowing
=========

Shadowing is a phenomenon that occurs when both structures to be merged define the same key. In this case, the value in the overlaying structure "shadows" or hides the value of the underlaying structure. This means that the value from the overlaying structure will be used in the merged structure, while the value from the underlaying structure will not be visible.

For example, consider the following two structures:

.. code-block:: json

    {
        "underlay": {
            "key": "underlay value"
        },
        "overlay": {
            "key": "overlay value"
        }
    }

If we merge the underlay and overlay objects, the resulting structure would be:

.. code-block:: json

    {
        "key": "overlay value"
    }

In this case, the value of the key field in the underlaying structure is "shadowed" or hidden by the value of the same field in the overlaying structure. As a result, the value from the overlaying structure is used in the merged structure, while the value from the underlaying structure is discarded at this layer.

It's worth noting that shadowing can occur at any level of the structure, not just at the top level. For example, if the underlay and overlay structures were 
both nested objects, shadowing could occur at any level of the nested objects.
