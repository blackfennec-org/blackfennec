.. _definition_type_registry:
.. _type_registry:

"""""""""""""
Type Registry
"""""""""""""
The Type Registry is a register of all known (aka registered) :ref:`Types <definition_type>`. Types which are not known to the type registry cannot be considered in the :ref:`selection process <definition_selection_process>`. The type registry is accessible to extensions via :ref:`Extension API <definition_extension_api>`.


.. uml::

    hide circle
    hide members
    hide methods

    skinparam class {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
    }

    class "Extension Api" as api    
    class "Interpretation Service" as is
    class "TypeRegistry" as tr
    class "Type" as t

    api --> tr : references
    is --> tr : uses
    tr --> t : contains

