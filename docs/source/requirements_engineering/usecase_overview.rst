UseCase Overview
================


.. uml::

    @startuml
    left to right direction

    skinparam usecase {
      BackgroundColor White
      BorderColor Black
      ArrowColor Black
      ActorBackgroundColor Blue
      ActorBorderColor Pink
    }

    actor Matthew as m
    note left of m : Web Dev, Easy of Use

    actor Katja as k
    note left of k : Prof. Data Analytics, Visualisation

    actor Sun as s
    note left of s : Secruty Specialist, OSINT

    actor Alan as a
    note left of a : Extension Dev., Flexibility

    package "Black Fennec" {
      usecase "Open Project" as open
      usecase "See interpreted Data" as InterpretedData
      usecase "Best available Representation" as bestfit
      usecase "Save Changes" as save
      usecase "Collaborate with Others" as collab
      usecase "Import Data into Project" as import
      usecase "Edit Data" as edit
      usecase "Manage Extensions" as ManExt
      usecase "Find Structure" as search
      usecase "Automate Task" as actions
    }
    package "Extension" {
      usecase "Develop Extension" as DevelopExtension
      usecase "Publish Extension" as PublishExtension
      usecase "Interact with Black Fennec" as InteractWBF
    }

    k --> collab
    s --> actions
    a --> ManExt
    k --> search


    a --> DevelopExtension
    a --> PublishExtension
    a --> InteractWBF
    @enduml