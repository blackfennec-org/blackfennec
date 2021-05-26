Project Plan
============

Introduction
************

Objective
---------
The purpose of this document is to describe the project plan and provide an overview of the Black-Fennec project.
This document contains a rough overview of our project, the project organization, and management processes.
It also includes risk management and some brief information about the infrastructure.

The project plan serves as a basis for the upcoming documents.

Scope
-----
The scope of this project is limited to the duration of the module Engineering Project FS2021.

References
----------
In the table below you can find the links to the important documents in the repository.

.. table::
  :align: left
  :widths: auto

  =========================  =============
  **Document**               **Reference**
  =========================  =============                   
  Project Proposal           :doc:`project_proposal`
  Risk Analysis              :doc:`risk_analysis`
  Definition of done         :doc:`/project_standards/definition_of_done`
  Logging Standards          :doc:`/project_standards//logging_standards`
  Version Control Strategy   :doc:`/project_standards//version_control_strategy`
  Version Control Strategy   :doc:`/project_standards//definition_of_scrum`
  =========================  =============

Project Overview
****************
Black Fennec is going to be an application that is able to manage unstructured data by interpreting information
compositions known to its type system. These interpretations are then visualised. The type system in its nature is a
weak typed dynamic object model that can be extended easily. To support specialised use cases and allow rapid
development Black Fennec provides an extension api. With the final product one will be capable of visualising and
editing any JSON and YAML files in a more productive way. A close integration of git allows for collaboration and data
sharing over existing infrastructure.

Purpose & Objectives
--------------------
The Objective is to have a usable product for data management in our toolset that can be maintained and enhanced for an
extended period of time. Therefore the quality of our architecture is of utmost importance.

We will use Black Fennec mainly as a data editing and visualisation tool that allows us to collaborate.

Our hopes are that the project will inspire a community to develop extensions and find use cases that we currently cant even
envision. For this we intend to release our source code into the public domain.

To address our personal goals, we intend to utilise and reinforce the knowledge gained during our studies.
Simultaneously we hope to learn many new principles and patterns.

Scope of Delivery
-----------------
The following table defines the scope of delivery of the black fennec project.

+--------------------------------------+--------------------------+
| Documentation                        | Product                  |
+--------------------------------------+--------------------------+
| - Project Proposal                   | - Software build         |
| - Project Plan                       | - Source Code            |
| - Risk Analysis                      | - Product Demonstration  |
| - Domain Analysis                    |                          |
| - Architecture Diagram               |                          |
| - Package/Class Design               |                          |
| - Code Guidelines                    |                          |
| - Test Specification/Test Protocol   |                          |
| - Protocol notes                     |                          |
+--------------------+-----------------+--------------------------+

Assumptions & Limitations
-------------------------
We expect to accomplish our core objectives before the delivery date. If time permits we will implement further
extensions which add additional use cases. These extensions are not part of the engineering project but could be
featured in the presentation to show the extensibility and usability of the project.

Project Organisation
********************

Organisational Structure
------------------------
To manage our project we use Scrum roles and additionally assigned competences to each member. Additionally every member of the team acts as a developer and will contribute code to the project.

================  ===================================
Team Members            Competences
================  ===================================
Lara Gubler       Scrum Master, Documentation
Simon Kindhauser  Product Owner, Architecture
Leonie Däullary   Development Team, User Experience
Caspar Martens    Development Team, Quality Assurance
================  ===================================

.. _project_manager:
Project Manager
^^^^^^^^^^^^^^^
The management of the project which includes the scheduling of meeting with stakeholders, and the organisation of development-team internal meetings is in this project done by the role of the Scrum Master which is Lara Gubler.

Project Management
******************

Time Budget
-----------
+------------------------------+---------------------+
| **Project duration**         | 14 Weeks            |
+------------------------------+---------------------+
| **Team members**             | 4 Persons           |
+------------------------------+---------------------+
| **Working hours per person** | 120h                |
+------------------------------+---------------------+
| **Total hours of work**      | 480h                |
+------------------------------+---------------------+
| **Project start**            | 22. February 2021   |
+------------------------------+---------------------+
| **Project end**              | 28. May 2021        |
+------------------------------+---------------------+

Time Management
---------------
We use Gitlab to track the time estimated and spent time of our work items represented as issues. Fine grained
time management will be conducted before each sprint (lasting two weeks).

Phases
^^^^^^
The phases that exist in our Project are taken from the Rational Unified Process Framework and consist of the Phases:

- Inception
- Elaboration
- Construction
- Transition

These Phases do not have a fix duration in our Setup and are evaluated during the planning of the Scrum Sprints. This means no definite duration will be provided here.

Iterations
^^^^^^^^^^
The iterations during this project are represented by Scrum Sprints. They endure 2 Weeks and are lead by our Product Owner (Simon Kindhauser) and the Scrum Master (Lara Gubler). A more detailed elaboration of our Scrum processes can be found in the chapter Meetings_.

.. _project_timeline:
Project Timeline
^^^^^^^^^^^^^^^^
.. uml:: project_timeline.puml

The blue arrows in the milestone section show when Milestones with respecting reviews are planned in our project. As this plan is in the future the red arrows indicate the scope of the time-window in which they should be fulfilled.

During the Elaboration phase a more detailed plan for the Construction phase has been created. It can be found in the :doc:`elaboration` document.

Milestones
^^^^^^^^^^

Here in this Document we provide only an overview of the Milestones that exist in our Project in a chronological ordering. At the time this Document is created not all Milestones are already planned to the end. Therefore a link is provided that allows to look at the Milestone in Gitlab which always contains the most timely information. Definite dates and additional deliverables will be defined when appropriate.

===============================================================  ==============================================================
 Milestone                                                       Link
===============================================================  ==============================================================
R0: Project Proposal (Inception)                                 `Milestone: Project Proposal <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/8>`_
R1: Project Plan (Inception)                                     `Milestone: Project Plan <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/1>`_
R2: Requirements Engineering (Elaboration)                       `Milestone: Requirements <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/2>`_
R3: End of Elaboration & Architecture Prototype (Elaboration)    `Milestone: End of Elaboration <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/3>`_
R4: Architecture (Construction)                                  `Milestone: Architecture <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/4>`_
R5: Q-Review (Transition)                                        `Milestone: Q-Review <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/5>`_
Final Submission                                                 `Milestone: Final Submission <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/6>`_
Project Presentation                                             `Milestone: Project Presentation <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/7>`_
===============================================================  ==============================================================

Meetings
--------
During our project, various Scrum meetings are held. These always take place on the same day, at the same time, so that all members can plan and prepare for them in advance. The definition and scope of the meetings is documented in our :doc:`/project_standards/definition_of_scrum`.


Meetings Timetable
^^^^^^^^^^^^^^^^^^
In the following table one can see how we have scheduled the meetings.

=====================  =================================  =======================  ========================
 Meetings Timetable     | Friday 1                         | Friday 2               | Friday 3
=====================  =================================  =======================  ========================
 08:00 - 09:00          Daily Scrum                        Daily Scrum              Daily Scrum
 09:00 - 10:00
 10:00 - 11:00          Sprint Review (previous sprint)                             Sprint Review
 11:00 - 12:00          Milestone Meeting (previous)                                Milestone Meeting
 12:00 - 13:00
 13:00 - 14:00          Sprint Planning                    Daily Scrum
 15:00 - 15:00
 15:00 - 16:00
 16:00 - 17:00                                             Sprint Retrospective
=====================  =================================  =======================  ========================

Each Sprint consists of two weeks of time but is spread over 3 weeks. A new iteration starts at midday and ends two weeks later before a potential milestone meeting. This accommodates working on weekdays before friday.

The Daily Scrum meetings are held twice a day in the middle week to ensure productivity and resolve potential issues faster.

Protocolling
^^^^^^^^^^^^
For each meeting a protocol is created. These record what we discussed in the meeting, what decisions were made and any open issues. They are represented by Gitlab issues which also allow time tracking.

Risk Management
---------------
We continuously assess risks and deduce mitigation strategies based on processes described in ISO 27005, specifically assigning the risk one of the following categories:

* reduce
* retain
* avoid
* transfer 

Risk Analysis
^^^^^^^^^^^^^
A list of all identified risks can be found in the document :doc:`risk_analysis`. The most important findings as of the writing of this document are listed below.

Complexity
  The mitigation strategy is effective but the issue must be reevaluated regularly to proactively intervene in a timely manner.

User Experience
  We dedicate a member of the team to the issue. However, the remaining risk is still significant and we will collectively keep an eye on it.

Quality Assurance
-----------------
To ensure the desired quality in this project many different standards are enforced. For a detailed account read the document :doc:`/project_standards/quality_assurance`.

The basis of our quality assurance is the use of frequent and builtin meetings. How these are scheduled is described in the `Meetings Timetable`_. These meetings are held in accordance with our :doc:`/project_standards/definition_of_scrum` and help to ensure quality and efficiency in our code and processes. Additionally, we deploy code reviews and rigorous testing, pair programming and the "gitflow".


Infrastructure
**************

GitLab
------
GitLab is a tool which we use for multiple aspects in our project. For example for the management of our source code
and documents. We also use it for our version controlling and to plan our project. Our work items are stored in the
GitLab repository in the form of issues.

PyCharm
-------
For the integrated development environment (IDE) we use PyCharm from JetBrains.
This is a very useful tool for Python programming and includes some useful git functionalities such as commit,
push and merge.

PyTest
------
As our testing framework we use pytest that allows easy to write unit tests but meanwhile also support more complex tests if required. Additionally to test running it is also able to generate a coverage analysis that can be integrated with Gitlab.

PyLint
------
Pylint is the linter used for our project. It can check for logical errors and formatting. The formatting guidelines used are close to the PEP 8 but differs in minor aspects. A plugin for an easy integration with the IDE PyCharm exists and is used.

Glade
-----
For our graphical user interface (GUI) we use Glade. Glade is a rapid application development tool (RAD) and allows us to quickly and easily develop user interfaces for the GTK toolkit

GTK
---
GTK is a free and open-source cross-platform widget toolkit. We use it to develop our Black Fennec app.



