.. _observable_layer:

================
Observable Layer
================

The Observable Layer is a feature that allows you to monitor changes to a structure. It does not modify the structure in any way, but instead adds observability to changes made to the structure by other entities. This means that any observer registered with the Observable Layer will be notified every time a change is made to the structure.

One practical application of the Observable Layer is in the implementation of an "undo" and "redo" function. The :ref:`History Service <history_service>`, for example, can use the observable layer to track changes made to a structure and allow users to undo or redo those changes as needed.

Here's an example of how the Observable Layer might be used:

.. code-block:: python

    # same as above but in Python using Black Fennec API

    structure = Map({
        "key": String("initial value")
    })

    layer = ObservableLayer()
    observed_structure = layer.apply(structure)

    def on_change(sender, notification):
        print(f"Structure has been updated to: {notification.new_value}")

    observed_structure.bind(changed=on_change)

    structure["key"] = String("new value")

    # Output: "Structure has been updated to: { key: 'new value' }"



In this example, we create a new Observable Layer using an existing structure as the base. We then subscribe to changes to the structure using the ``bind()`` method. When we update the structure by changing the value of the key field, the observable layer notifies our observer, causing the callback function to be executed.

Overall, the Observable Layer is a powerful tool for tracking changes to a structure and reacting to those changes in real-time.
