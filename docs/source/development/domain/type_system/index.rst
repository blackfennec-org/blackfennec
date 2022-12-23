.. _definition_type_system:

===========
Type System
===========

The Type System in Black Fennec is responsible for defining and managing the various types that are used in the application. It consists of several key components, including the Type Registry, Type Parser, and Interpretation Service.

The Type System also includes various types themselves, such as Map Type, List Type, String Type, Number Type, Boolean Type, Null Type, and Reference Type. These types define the characteristics and behavior of the values they represent, and are used to ensure that values are stored and processed correctly within the application.

.. uml:: type_system.puml

The Type Registry is a database of registered Types, which is used to store and manage the available types in the application. The Type Parser is responsible for parsing type definitions and creating new Types, while the Interpretation Service is responsible for interpreting values and mapping them to the appropriate Type.

.. toctree::
    :caption: Table of Contents
    :maxdepth: 2

    type
    type_registry
    interpretation/index
    loading_types
