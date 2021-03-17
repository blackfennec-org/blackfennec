Non-Functional Requirements
===========================

Overview
********
.. uml:: non_functional_overview.puml

Detailed Description
********************

Template
--------
===============  ==================
**Title (ID)**   NFR-1
**Scenario**     Do sth.
**Stimulus**     Event or Action
**Expectation**  Reaction
**Measure**      Measurement
===============  ==================

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
===============  ==================
**Title (ID)**   Interface Documentation
**Scenario**     Developer wants to lookup something in the Documentation
**Stimulus**     The Developer does not understand how two components interact with each other
**Expectation**  Both components and their interaction, if any, can be found in the documentation
**Measure**      Interfaces and classes important to an external developer are documented.
===============  ==================

TODO: NFR
The documentation provides a reasonable overview over the domain model and architecture of the project. Application programming interfaces are well defined and allow for rapid development of connected systems.

Well Tested
~~~~~~~~~~~
===============  ==================
**Title (ID)**   Unit-Testing
**Scenario**     A new feature for the application is required
**Stimulus**     Developer adds new source code to the project
**Expectation**  Code coverage does not decrease significantly. The goal of the new feature is tested on fulfillment. Unit-tests cover equivalence classes and boundaries.
**Measure**      Merge Request with Assignee and Reviewer prevent code to be merged without Testing.
===============  ==================

===============  ==================
**Title (ID)**   Regression-Testing
**Scenario**     A preexistent feature for the application has to be changed
**Stimulus**     Developer changes source code of the project
**Expectation**  The goal of the feature adaptation is tested on fulfillment. Old usage of the code keeps working as expected. Errors that were fixed before are not reintroduced.
**Measure**      When Bugs are fixed a new testcase has to be created. A CI/CD Pipeline Test commited code on quality measures and runs the unit-tests of the project.
===============  ==================

TODO: NFR
The application is well tested. This includes unit tests, integration test, system tests etc.

Completeness
~~~~~~~~~~~~

===============  ==================
**Title (ID)**   NFR-Fulfillment
**Scenario**     The Application is used by the client (Team/PO)
**Stimulus**     A demonstration before the release in the productive environment is done
**Expectation**  No unexpected exceptions happen when using the final product. All NFRs required for a successful usage of the application are fulfilled.
**Measure**      System tests try to measure the fulfillment of functional and non-functional-requirements. Each NFR if feasible is featured in the system-testing protocol to test its fulfillment.
===============  ==================

TODO: NFR
The functional requirements have been implemented to the satisfaction of the client (the team/product owner) 

Availability
^^^^^^^^^^^^

Internet Dependence
~~~~~~~~~~~~~~~~~~~

===============  ==================
**Title (ID)**   Internet-Dependence
**Scenario**     A user is using the application
**Stimulus**     The device used by the user looses connection to the internet
**Expectation**  Changes that require to be synchronized to a remote platform can be saved locally and later explicitly uploaded to a shared resource.
**Measure**      File-sharing is done using git, which comes with capabilities to ensure offline saving and distribution of files in dedicated moments.
===============  ==================

The application is usable without the need for a functioning internet connection. Changes that require to be synchronized to a remote platform can be saved locally and later explicitly uploaded to a shared resource.

Fault Tolerance
^^^^^^^^^^^^^^^
Handling Exceptions
~~~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Exception-Handling
**Scenario**     A user is using the application
**Stimulus**     An exception is thrown
**Expectation**  The application keeps running. The user is displayed a meaningful error message. The exception is logged, and allow to draw conclusions on why the error happened
**Measure**      Any exception is captured on application level and printed in a dedicated window. In code review of merge requests exceptions are looked at to ensure sufficient logging is done.
===============  ==================

TODO: NFR
Exceptions do not result in the immediate shutdown of the system. In the minimum a meaningful error message is displayed to the user and the logs document the context of the failure(?).

Recoverability
^^^^^^^^^^^^^^
===============  ==================
**Title (ID)**   Malformed-Configuration
**Scenario**     A user opens the application
**Stimulus**     invalid configuration or invalid module causes a software failure
**Expectation**  The application can be started even if the configuration file is malformed.
**Measure**      A recovery mode (no extensions loaded) allows the loading of valid files which can be parsed, edited and analysed.
===============  ==================

TODO: NFR
The application can be started even if the configuration file is malformed. A recovery mode (no extensions loaded) allows the loading of valid files which can be parsed, edited and analysed.

Performance Efficiency
----------------------
Time Behaviour
^^^^^^^^^^^^^^

Fast Starter
~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Application-Start
**Scenario**     A user wants to work with the application
**Stimulus**     A user opens the application
**Expectation**  A loading screen shows the status of the application to the user. As soon as the preparatory tasks are done, the main window opens. Operations that take a long time are done after the start of the application.
**Measure**      The application starts within 500ms of clicking the icon on a consumer laptop (intel i5 8th gen + 8gb ram) IF no additional extensions are installed.
===============  ==================

The application starts within 500ms of clicking the icon on a consumer laptop (intel i5 8th gen + 8gb ram). The display of a loading screen suffices to satisfy this requirement IFF updated status information is provided to the user. 

Loading Projects
~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Project-Loading
**Scenario**     A user wants to enter data or visualise a file
**Stimulus**     A file is loaded by the user
**Expectation**  The file opens and the data is displayed in the first meaningful view.
**Measure**      With a medium sized file (500 MB) it should take no more than 800ms if the reference implementation of the presenter is used.
===============  ==================
Loading a medium sized project (TBA) takes no more the 800ms before the reference implementation of the presenter can display the first meaningful view.

Quick Save
~~~~~~~~~~
===============  ==================
**Title (ID)**   Project-Saving
**Scenario**     A user wants to save the changes made to a file locally
**Stimulus**     The user triggers the save option
**Expectation**  The changed data is saved into the currently open file.
**Measure**      Saving a medium sized project with X (TBA) changes takes no longer than 1000ms.
===============  ==================
Saving a medium sized project with X (TBA) changes takes no longer than 1000ms.

Flash Decision
~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Type-Selection
**Scenario**     A user has data that can be interpreted in multiple ways
**Stimulus**     The user selects a type for the visualised data
**Expectation**  The visualisation changes to show the selected type
**Measure**      With a core data-type it should take no more than 150ms. More advanced types such as lists take no more than 300ms
===============  ==================

Selecting the type for a structure takes no more then 200ms.

Resource Utilisation
^^^^^^^^^^^^^^^^^^^^
Capacity
^^^^^^^^
Heavy Lifter
~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Project-Loading-Limits
**Scenario**     A user wants to enter data or visualise a file of large extent
**Stimulus**     A large file is loaded by the user
**Expectation**  The file opens and the data is displayed in the first meaningful view.
**Measure**      With a large sized file (1 GB) it should be possible to open it in TBA if the reference implementation of the presenter is used.
===============  ==================
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