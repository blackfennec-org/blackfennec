.. _history_service:

===============
History Service
===============

The History Service is a system that allows users to undo and redo actions within the Structure. It works by tracking changes made to a data structure and storing a history of those changes. The History Service typically makes use of the :ref:`Observable Layer <observable_layer>`, which allows it to monitor changes to an entire :ref:`Structure <definition_structure>` and store a history of those changes. When the user requests an "undo" or "redo" action, the History Service uses this history to revert the structure to a previous state or move forward to a later state.

Here's an example of how the History Service might be used to offer "undo" and "redo" functionality in a UI:

.. code-block:: python

    structure = Map({
        "key": String("initial value")
    })

    layer = ObservableLayer()
    observable_structure = layer.apply(structure)

    history_service = HistoryService(layer)

    # Register a change to the structure
    structure["key"] = String("new value")

    # Undo the last change
    history_service.undo()

    print(structure["key"])
    # Output: "initial value"

    # Redo the last change
    history_service.redo()

    print(structure["key"])
    # Output: "new value"


In this example, we create a new Observable Layer using an existing Structure as the base, and we create a new History Service using the Observable Layer as the source of change history. We then register a change to the Structure by updating the value of the key field. When we call the ``undo()`` method on the History Service, it reverts the Structure to its previous state, changing the value of the key field back to "initial value". When we call the ``redo()`` method, the Structure is restored to its original state with the value of the key field set to "new value".

Overall, the History Service is an essential tool for implementing "undo" and "redo" functionality in a UI, allowing users to easily revert or repeat actions as needed.
