Non-Functional Requirements
===========================

Overview
********
.. uml::non_functional_overview.puml

Detailed Description
********************

Functional Suitability
----------------------
Completeness
^^^^^^^^^^^^
Correctness
^^^^^^^^^^^
Appropriateness
^^^^^^^^^^^^^^^

Reliability
-----------
Maturity
^^^^^^^^
Good Documentation
~~~~~~~~~~~~~~~~~~
TODO: NFR
The documentation provides a reasonable overview over the domain model and architecture of the project. Application programming interfaces are well defined and allow for rapid development of connected systems.

Well Tested
~~~~~~~~~~~
TODO: NFR
The application is well tested. This includes unit tests, integration test, system tests etc.

Completeness
~~~~~~~~~~~~
TODO: NFR
The functional requirements have been implemented to the satisfaction of the client (the team/product owner) 

Availability
^^^^^^^^^^^^

Fault Tolerance
^^^^^^^^^^^^^^^
Handling Exceptions
~~~~~~~~~~~~~~~~~~~
TODO: NFR
Exceptions do not result in the immediate shutdown of the system. In the minimum a meaningful error message is displayed to the user and the logs document the context of the failure(?).

Recoverability
^^^^^^^^^^^^^^
TODO: NFR
The application can be started even if the configuration file is malformed. A recovery mode (no extensions loaded) allows the loading of valid files which can be parsed, edited and analysed.

Performance Efficiency
----------------------
Time Behaviour
^^^^^^^^^^^^^^

Fast Starter
~~~~~~~~~~~~
The application starts within 500ms of clicking the icon on a consumer laptop (intel i5 8th gen + 8gb ram). The display of a loading screen suffices to satisfy this requirement IFF updated status information is provided to the user. 

Loading Projects
~~~~~~~~~~~~~~~~
Loading a medium sized project (TBA) takes no more the 800ms before the reference implementation of the presenter can display the first meaningful view.

Quick Save
~~~~~~~~~~
Saving a medium sized project with X (TBA) changes takes no longer than 1000ms.

Flash Decision
~~~~~~~~~~~~~~
Selecting the type for a structure takes no more then 200ms.

Resource Utilisation
^^^^^^^^^^^^^^^^^^^^
Capacity
^^^^^^^^
Heavy Lifter
~~~~~~~~~~~~
The application can open projects of at least 1GB of raw data (excluding binary data like images and videos).

Compatibility
-------------
Co-existence
^^^^^^^^^^^^
Git Integration
~~~~~~~~~~~~~~~
Projects can be version controlled using git.

Json as a Service
~~~~~~~~~~~~~~~~~
Projects can be exported and imported to and from JSON files.

Interoperability
^^^^^^^^^^^^^^^^

Usability
---------
Appropriateness
^^^^^^^^^^^^^^^

Data Aggregation
~~~~~~~~~~~~~~~~
The application is appropriate when collecting data from various sources.

Data Visualisation
~~~~~~~~~~~~~~~~~~
The application is appropriate when visualising interconnected data.

Learnability
^^^^^^^^^^^^
Just Like an Apple
~~~~~~~~~~~~~~~~~~
The application make intuitive sense to new users.


Operability
^^^^^^^^^^^
User Error Protection
^^^^^^^^^^^^^^^^^^^^^
Better than Hawaii
~~~~~~~~~~~~~~~~~~
Actions which are hard to revert are also hard to perform by accident. Execution of such commands might be delayed for a few seconds allowing cancellation.

User Interface Aesthetics
^^^^^^^^^^^^^^^^^^^^^^^^^
Something something style guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GTK?

Accessibility
^^^^^^^^^^^^^
Stolze Spezial
~~~~~~~~~~~~~~
Text and Labels are readable even for people with difficulties seeing colours or contrast. And the two senses principal is adhered.

Security
--------
Confidentiality
^^^^^^^^^^^^^^^

Sand Box
~~~~~~~~
The application is sandboxed for the operating system... This is optional but desirable.

Integrity
^^^^^^^^^
The Corruption of the Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Files won't be corrupted.

Non-repudiation
^^^^^^^^^^^^^^^
Authenticity
^^^^^^^^^^^^
Accountability
^^^^^^^^^^^^^^

Maintainability
-----------------
Modularity
^^^^^^^^^^
Reusability
^^^^^^^^^^^
Analyzability
^^^^^^^^^^^^^
Modifiability
^^^^^^^^^^^^^
Windows is Broken. Long live Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clean Code and Broken Window Theory i guess.

Testability
^^^^^^^^^^^

Portability
-----------
Adaptability
^^^^^^^^^^^^
Installability
^^^^^^^^^^^^^^

Pip Install via setup.py (for devs) and gitlab PyPI


Replaceability
^^^^^^^^^^^^^^

Hail JSON
~~~~~~~~~
Its replaceable because JSON. The application does not hide any state or information from its users. It is a pure convenience tool and must not be a necessity to access or modify data. Good night.