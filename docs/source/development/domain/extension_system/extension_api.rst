.. _definition_extension_api:
.. _extension_api:

=============
Extension Api
=============

The Extension API providing a way for :ref:`extensions <definition_extension>` to access various features and functionality within the application. It acts as an interface between extensions and the application, allowing extensions to interact with and utilize the available services and resources.

The Extension API consists of a collection of services. These services include, the :ref:`Interpretation Service <interpretation_service>`, the :ref:`Presenter Registry <presenter_registry>`, the :ref:`View Factory Registry <type_view_factory_registry>`, the :ref:`Action Registry <action_registry>`, the :ref:`Type Registry <type_registry>`, the :ref:`Mime Type Registry <mime_type_registry>`, and the :ref:`Resource Type Registry <resource_type_registry>`.

.. uml::

   @startuml Extension API

   skinparam class {
      BackgroundColor White
      BorderColor Black
      ArrowColor Black
   }

   hide circle
   hide members
   hide methods

   left to right direction


   title Extension API


   package "Black Fennec" <<Frame>> {
      package "Extension System" <<Frame>> {
         class "Extension" as e
         class "Extension API" as api

         e --> api: has access to
      }
      class "Interpretation Service" as is
      class "Presenter Registry" as pr
      class "View Factory Registry" as vfr
      class "Action Registry" as ar
      class "Type Registry" as typer
      class "Mime Type Registry" as mtr
      class "Resource Type Registry" as rtr

      api ---> is
      api ---> pr
      api ---> vfr
      api ---> ar
      api ---> typer
      api ---> mtr
      api ---> rtr

   }

   @enduml


The generated code documentation below provides a up-to-date description of the interface the Extension Api provides to extensions.

.. automodule:: blackfennec.extension_system.extension_api
   :noindex:
   :members:
   :undoc-members:
   :show-inheritance:
