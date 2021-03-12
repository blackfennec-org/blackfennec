UseCase Overview
================


.. uml::

    @startuml
    left to right direction

    actor User as u
    actor Developer as d
    package "Black Fennec" {
      usecase "Load File" as LoadFile
      usecase "Edit File" as EditFile
      usecase "Save File" as SaveFile
      usecase "Import File" as ImportFile
      package "git" {
        usecase "Select File" as SelectFile
        usecase "Pull File" as PullFile
        usecase "Commit File" as CommitFile
        usecase "Push File" as PushFile
      }

    }
    u --> LoadFile
    u --> EditFile
    u --> SaveFile
    u --> ImportFile
    u --> SelectFile
    u --> CommitFile
    u --> PullFile
    u --> PushFile
    @enduml