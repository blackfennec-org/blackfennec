.. _definition_overlay:
.. _overlay_adapter:

=======
Overlay
=======

The responsibility of the Overlay is the resolutions of :ref:`References <definition_reference>`. The resulting layer thus replaces all references with the referenced object. This is best illustrated with an example.

A reference in JSON could look like this:

.. code-block:: JSON

    {
        "example": {
            "title": "Reference Resolution Example",
            "text": "This is an example of a reference resolution."
        },
        "reference": { "$ref": "#/example" }
    }

After applying the Overlay, the reference is resolved and the resulting :ref:`Structure <definition_structure>` feels like this:

.. code-block:: JSON

    {
        "example": {
            "title": "Reference Resolution Example",
            "text": "This is an example of a reference resolution."
        },
        "reference": {
            "title": "Reference Resolution Example",
            "text": "This is an example of a reference resolution."
        }
    }

Note, that it only __feels__ like this. In actuality there is no duplication of the object. The reference is resolved and replaced with a Python reference, thus changes are always visible in both places.

Since this feature is implemented in a :ref:`Layer <definition_layer>` it is non-destructive and the original data is not modified. This allows us to "recover" all used JSON references when saving the data.
