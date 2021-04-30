.. _definition_core_types:
.. _object_model:

The Object Model
================
Core :ref:`types <definition_type>` are the fundamental types. All other types are actually structures built with core types. The most commonly used structures are considered :ref:`base types <definition_base_types>`.

.. uml::
    
    @startuml

    hide circle
    hide members
    hide methods

    skinparam class {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
    }
    
    package "Core Types" {
        class Information {}
        class Number {}
        class String {}
        class List {}
        class Map {}
        class Reference {}
        class Root {}

        Information     -->         Information     : parent
        Information     -up->       Root            : root
        Number          --|>        Information     
        String          --|>        Information
        List            -right-|>   Information
        List            --> "0..*"  Information 
        Map             -up-|>      Information
        Map             --> "0..*"  Information
        Reference       -up-|>      Information
        Reference       --> "0..1"  Information
        Root            -->         Root            : root
    }
    @enduml
    


Information
"""""""""""
All types hold information. Functionality common among all core types is placed here. All core types inherit from information.

Parent of Information
~~~~~~~~~~~~~~~~~~~~~
The parent of an information is closer to the root in the :ref:`tree <definition_underlay>`.

Root of Information
~~~~~~~~~~~~~~~~~~~
The root information is the root of the :ref:`tree <definition_underlay>` and the starting point of absolute paths.

Number
""""""
This core type represents numbers including integers and floating points.

String
""""""
This core type represents strings (e.g. "hello world"). It is also used for longer texts.

.. _definition_type_list:

List
""""
A list is a collection of information.


Map
"""
A map is a collection of key-value pairs of information.

.. _definition_type_reference:

Reference
"""""""""
A reference is an absolute or relative path to information. This type only exists on the :ref:`underlay <definition_underlay>` and is not visible on higher :ref:`layers <definition_layer>`.

Root
""""
The root is special as it is unique in a :ref:`tree <definition_underlay>`. It can be any type of information and differs only in that it is its own parent.

Absolute paths of references start from the root.
