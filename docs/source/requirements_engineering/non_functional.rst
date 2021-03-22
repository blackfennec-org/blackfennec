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
===============  ==================
**Title (ID)**   Interface Documentation
**Scenario**     A user wants to perform a certain action.
**Stimulus**     Black Fennec handles the action as expected.
**Expectation**  Black Fennec provides the correct results with the needed degree of precision.
**Measure**      At least 85% of the code has to be covered by Unit Tests which are successful.
===============  ==================

The degree to which a product or system provides the correct results with the needed degree of precision
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
**Stimulus**     The Developer does not understand how two components interact with each other.
**Expectation**  Both components and their interaction, if any, can be found in the documentation.
**Measure**      Merge requests are checked for sufficient documentation of added functionality.
**Criteria**     Interfaces and classes important to an external developer are documented.
===============  ==================

TODO: NFR
The documentation provides a reasonable overview over the domain model and architecture of the project. Application programming interfaces are well defined and allow for rapid development of connected systems.

Well Tested
~~~~~~~~~~~
===============  ==================
**Title (ID)**   Unit-Testing
**Scenario**     A new feature for the application is required.
**Stimulus**     Developer adds new source code to the project.
**Expectation**  Code coverage does not decrease significantly. The goal of the new feature is tested on fulfillment. Unit-tests cover equivalence classes and boundaries.
**Measure**      Merge Request with Assignee and Reviewer prevent code to be merged without Testing.
**Criteria**     Test coverage above 90 %.
===============  ==================

===============  ==================
**Title (ID)**   Regression-Testing
**Scenario**     A preexistent feature for the application has to be changed
**Stimulus**     Developer changes source code of the project
**Expectation**  The goal of the feature adaptation is tested on fulfillment. Old usage of the code keeps working as expected. Errors that were fixed before are not reintroduced.
**Measure**      When bugs are fixed a new testcase has to be created. A CI/CD pipeline test commited code on quality measures and runs the unit-tests of the project.
**Criteria**     All unit-tests succeed.
===============  ==================

TODO: NFR
The application is well tested. This includes unit tests, integration test, system tests etc.

Completeness
~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Requirements-Fulfillment
**Scenario**     The Application is used by the client (Team/PO)
**Stimulus**     A demonstration before the release in the productive environment is done
**Expectation**  No unexpected exceptions happen when using the final product. All NFRs required for a successful usage of the application are fulfilled.
**Measure**      System tests try to measure the fulfillment of functional and non-functional-requirements.
**Criteria**     Each Requirement if feasible and untested with unit-test is featured in the system-testing protocol to test its fulfillment.
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
**Criteria**     Any feature requiring internet connection provides offline alternative or meaningful error message.
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
**Measure**      In code review of merge requests exceptions are looked at to ensure sufficient logging is done.
**Criteria**     Any exception is captured on application level and printed in a dedicated window.
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
**Criteria**     Application starts despite malformed config
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
**Expectation**  A loading screen shows the status of the application to the user. As soon as the preparatory tasks are done, the main window opens.
**Measure**      First operation is showing the loading screen which is capable of showing the status of the operation in progress
**Criteria**     The application/loading screen starts within 500ms of clicking the icon on a consumer laptop (intel i5 8th gen + 8gb ram) IF no additional extensions are installed.
===============  ==================

The application starts within 500ms of clicking the icon on a consumer laptop (intel i5 8th gen + 8gb ram). The display of a loading screen suffices to satisfy this requirement IFF updated status information is provided to the user. 

Loading Projects
~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Project-Loading
**Scenario**     A user wants to enter data or visualise a file
**Stimulus**     A file is loaded by the user
**Expectation**  The file opens and the data is displayed in the first meaningful view.
**Measure**      Only first meaningful view displayed, succeeding operations done afterwards.
**Criteria**     With a medium sized file (500 MB) it should take no more than 800ms if the reference implementation of the presenter is used.
===============  ==================

Loading a medium sized project (TBA) takes no more the 800ms before the reference implementation of the presenter can display the first meaningful view.

Quick Save
~~~~~~~~~~
===============  ==================
**Title (ID)**   Project-Saving
**Scenario**     A user wants to save the changes made to a file locally
**Stimulus**     The user triggers the save option
**Expectation**  The changed data is saved into the currently open file.
**Measure**      Efficient JSON serialisation with dedicated library.
**Criteria**     Saving a medium sized project with X (TBA) changes takes no longer than 3000ms.
===============  ==================

Saving a medium sized project with X (TBA) changes takes no longer than 1000ms.

Flash Decision
~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Type-Selection
**Scenario**     A user has data that can be interpreted in multiple ways
**Stimulus**     The user selects a type for the visualised data
**Expectation**  The visualisation changes to show the selected type
**Measure**      Evt. lazy loading to improve performance.
**Criteria**     With a core data-type it should take no more than 150ms. More advanced types such as lists take no more than 300ms. Extension types are out of scope.
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
**Scenario**     A user wants to enter data or visualise a file of large extent.
**Stimulus**     A large file is loaded by the user.
**Expectation**  The file opens and the data is displayed in the first meaningful view.
**Measure**      Large operations done after showing the first meaningful view. A loading screen also counts as meaningful view.
**Criteria**     With a large sized file (1 GB) it should be possible to open it in 5000ms if the reference implementation of the presenter is used.
===============  ==================

The application can open projects of at least 1GB of raw data (excluding binary data like images and videos).

Compatibility
-------------
Co-existence
^^^^^^^^^^^^
Git Integration
~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Git-Integration
**Scenario**     A user wants share files with other users
**Stimulus**     The user prefers the git console over the git-integration in the application and uses it
**Expectation**  The application detects changes to its working directory and adjusts relevant data
**Measure**      The file system is watched by the application for changes out of scope and copes with them
**Criteria**     Changed branches, pulling and conflicts are recognized.
===============  ==================

Projects can be version controlled using git.

Json as a Service
~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Project-Export
**Scenario**     A user wants to export his project to share with another user including all his settings
**Stimulus**     The user exports the project on a certain level (underlay/overlay)
**Expectation**  The project is exported including all settings of the user.
**Measure**      Mechanism to create interpretation of project data into exported file. Save black-fennec version to project file, to allow conversion to newer format.
**Criteria**     Setting of user compatible with version of importing application are respected.
===============  ==================

===============  ==================
**Title (ID)**   Project-Import
**Scenario**     A user wants to import a project file another user gave him.
**Stimulus**     The user imports external project
**Expectation**  The setting of
**Measure**      Mechanism to interpret imported project data
**Criteria**     Setting of exported project compatible with version of importing application are respected.
===============  ==================

Projects can be exported and imported to and from JSON files.

Interoperability
^^^^^^^^^^^^^^^^

Work in External Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   No-Project-Context
**Scenario**     A user wants view/edit file in external directory
**Stimulus**     The user opens JSON file with black-fennec
**Expectation**  The file is interpreted and visualised without requiring a project context
**Measure**      No dependence on project settings. Check for sufficient rights, understandable error message shown if no permission.
**Criteria**     Original file is opened if permissions allow. Changes in file can be saved if permissions allow.
===============  ==================

Work with files of External Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Json-Import
**Scenario**     A user wants share files with other users that are encapsulated in directory used by others
**Stimulus**     The user imports external json into project
**Expectation**  The original file location is saved. The file is copied into the project
**Measure**      Check for sufficient rights, understandable error message shown if no permission
**Criteria**     Original file is not changed.
===============  ==================

===============  ==================
**Title (ID)**   Json-Export
**Scenario**     A user wants to export a file in his project to an external location
**Stimulus**     The user clicks to export a file of the project
**Expectation**  The file is exported without containing any black-fennec proprietary data
**Measure**      Check for sufficient rights, understandable error message shown if no permission
**Criteria**     File at location is overwritten. No proprietary data contained in exported file.
===============  ==================

Usability
---------
Appropriateness
^^^^^^^^^^^^^^^

Data Aggregation
~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Data-Aggregation
**Scenario**     A user wants to aggregate data from several sources into one file
**Stimulus**     The user open a new project and inputs external data
**Expectation**  The application allows the user an efficient workflow for aggregation of data
**Measure**      Dedicated presenters for different use cases to allow optimized workflows
**Criteria**     The most important functions are maximum two clicks away.
===============  ==================

The application is appropriate when collecting data from various sources.

Data Visualisation
~~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Data-Visualisation
**Scenario**     A user wants to look at interconnected data
**Stimulus**     The user opens a file containing interconnected data
**Expectation**  The application shows an overviewable visualisation of interconnected data
**Measure**      Dedicated presenter for visualisation of interconnected data (graph)
**Criteria**     interconnection of data visualised with lines in between data
===============  ==================

The application is appropriate when visualising interconnected data.

Learnability
^^^^^^^^^^^^
Just Like an Apple
~~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Intuitive-Application
**Scenario**     A user wants to work with black-fennec
**Stimulus**     The user opens the application for the first time
**Expectation**  The user can operate basic use cases after few minutes of using the application
**Measure**      Walk-through upon first opening of application. Manual for usage of application.
**Criteria**     Closed-card-sort and tree-sort passed with industry standards
===============  ==================

The application make intuitive sense to new users.


Operability
^^^^^^^^^^^
User Error Protection
^^^^^^^^^^^^^^^^^^^^^
Better than Hawaii
~~~~~~~~~~~~~~~~~~
===============  ==================
**Title (ID)**   Confirmation
**Scenario**     A user wants to perform a critical operation
**Stimulus**     The user clicks to perform a critical operation
**Expectation**  The user is asked whether he is not accidentally click said action
**Measure**      Show confirmation dialog before executing critical operation
**Criteria**     Confirmation dialog before performing critical actions
===============  ==================

===============  ==================
**Title (ID)**   Reversion
**Scenario**     A user wants to perform a critical operation
**Stimulus**     The user clicks to perform a critical operation
**Expectation**  The user is able to undo the critical action for a specified amount of time
**Measure**      Save previous state of application to rollback
**Criteria**     Critical actions can be roll-backed for at least 1m if possible
===============  ==================

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
===============  ==================
**Title (ID)**   Accessibility via screen reader
**Scenario**     A user wants to understand the interface without seeing it.
**Stimulus**     A user triggers the screen reading function.
**Expectation**  The screen reader understands the software interface and can translate text into speech.
**Measure**      All main functionalities are equipped with the text to speech "tag".
===============  ==================

Text and Labels are readable even for people with difficulties seeing colours or contrast. And the two senses principal is adhered.

Security
--------
Confidentiality
^^^^^^^^^^^^^^^

Sand Box
~~~~~~~~
===============  ==================
**Title (ID)**   Application Isolation
**Scenario**     A user imports malicious data into Black Fennec.
**Stimulus**     The Malicious code is executed inside the Black Fennec tool.
**Expectation**  The malicious data doesn't affect the OS.
**Measure**      Application can be executed in isolated environment.
===============  ==================

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
===============  ==================
**Title (ID)**   Clean Code
**Scenario**     A Developer develops low quality code for the sake of time.
**Stimulus**     The general code quality decreases.
**Expectation**  Developers pay attention to clean code and broken widows in development
**Measure**      Can be measured using pylint. Code will be reviewed before every merge.
===============  ==================

Clean Code and Broken Window Theory i guess.

Testability
^^^^^^^^^^^

Portability
-----------
Adaptability
^^^^^^^^^^^^
Installability
^^^^^^^^^^^^^^
===============  ==================
**Title (ID)**   Black Fennec Installation
**Scenario**     A user wants to install Black Fennec via the command line.
**Stimulus**     The user executes the pip install... command.
**Expectation**  The user can install the tool using the pip install command.
**Measure**      The user can start the Black Fennec Tool via the desktop icon.
===============  ==================

Pip Install via setup.py (for devs) and gitlab PyPI


Replaceability
^^^^^^^^^^^^^^

Hail JSON
~~~~~~~~~
Its replaceable because JSON. The application does not hide any state or information from its users. It is a pure convenience tool and must not be a necessity to access or modify data. Good night.