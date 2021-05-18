.. _definition_core_types:
.. _object_model:

The Object Model
================
The object model (also known as core :ref:`types <definition_type>`) defines the  fundamental types. All other types are structures built with it. The most commonly used structures are considered :ref:`base types <definition_base_types>` and are included in the base installation.

The object model is a DAG - apart from references - implemented with a composite pattern. It is possible to recognise this from the member of type Information in Lists and Maps. As for References, accessing the Information they point to is a special operation and References never has any children from the perspective of the DAG. Therefore, although they can break the DAG properties this is not their default behaviour. 

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
    
    package "Object Model" {
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
The root is special as it is unique in a :ref:`tree <definition_underlay>`. It can be of any type and differs only in that it is its own parent.

Absolute paths of references start from the root.
