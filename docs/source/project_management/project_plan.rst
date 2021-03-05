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

+--------------------------+---------------------------+
| **Document**             | **Reference**             |
+--------------------------+---------------------------+
| Project Proposal         | :doc:`project_proposal`   |
+--------------------------+---------------------------+
| Risk Analysis            | :doc:`risk_analysis`      |
+--------------------------+---------------------------+

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

Our hopes are that the project will inspire a community to develop extensions and find use cases that we currently cant
envision. For this we intend to release our sourcecode into the public domain.

To address our personal goals, we intend to utilise and reinforce the knowledge gained during our studies.
Simultaneously we hope to learn many new principles and patterns.

Scope of Delivery
-----------------
The following table defines the scope of delivery of the black fennec project.

+--------------------------------------+--------------------------+
| Documentation                        | Product                  |
+--------------------------------------+--------------------------+
| - Project Proposal                   | - Core Product           |
| - Project Plan                       | - Core Features          |
| - Risk Analysis                      | - Core GUI               |
| - Domain Analysis                    | - Base Extension         |
| - Architecture Diagram               | - Additional Extensions  |
| - Package-/Classdesign               | - Source Code            |
| - Code Guidelines                    |                          |
| - Testspecification/Testprotocol     |                          |
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
To manage our project we use scrum roles and additionally assigned competences to each member.

================  ===================================
Team Members            Competences
================  ===================================
Lara Gubler       Scrum Master, Documentation
Simon Kindhauser  Product Owner, Architecture
Leonie Däullary   Development Team, User Experience
Caspar Martens    Development Team, Quality Assurance
================  ===================================

Project Management
******************

Time Budget
-----------
+------------------------------+---------------------+
| **Project duration**         | 14 Weeks #TODO check|
+------------------------------+---------------------+
| **Team members**             | 4 Persons           |
+------------------------------+---------------------+
| **Working hours per person** | 120h                |
+------------------------------+---------------------+
| **Total hours of work**      | 480h                |
+------------------------------+---------------------+
| **Project start**            | 22. February 2021   |
+------------------------------+---------------------+
| **Project end**              | #TODO fill this out |
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
The iterations during this project are represented by Scrum Sprints. They endure 2 Weeks and are lead by our Product Owner (Simon Kindhauser) and the Scrum Master (Lara Gubler). A more detailed elaboration of our Scrum processes can be found in the chapter :ref:`Meetings`.

Milestones
^^^^^^^^^^

Here in this Document we provide only an overview of the Milestones that exist in our Project in a chronological ordering. At the time this Document is created not all Milestones are already planned to the end. Therefore a link is provided that allows to look at the Milestone in Gitlab which always contains the most timely information. Definite dates and additional deliverables will be defined when appropriate.

===============================================================  ==============================================================
 Milestone                                                       Link
===============================================================  ==============================================================
R0: Project Proposal (Inception)                                 `Milestone: Project Proposal <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/8>`
R1: Project Plan (Inception)                                     `Milestone: Project Plan <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/1>`
R2: Requirements Engineering (Elaboration)                       `Milestone: Requirements <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/2>`
R3: End of Elaboration & Architecture Prototype (Elaboration)    `Milestone: End of Elaboration <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/3>`
R4: Architecture (Construction)                                  `Milestone: Architecture <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/4>`
R5: Q-Review (Transition)                                        `Milestone: Q-Review <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/5>`
Final Submission                                                 `Milestone: Final Submission <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/6>`
Project Presentation                                             `Milestone: Final Submission <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/milestones/7>`
===============================================================  ==============================================================

Meetings
--------
During our project, various SCRUM meetings are held. These always take place on the same day, at the same time, so that
all members can plan and prepare for them in advance.

Daily SCRUM
^^^^^^^^^^^
This meeting will take place on each day that we will work together as a team on the project and will last about 15
minutes. It is mainly intended for the developers of our team.
During the meeting the progress towards the Sprint Goal will be reviewed. If necessary, the Sprint Backlog and the
planned work can be adjusted.

Sprint Planning
^^^^^^^^^^^^^^^
This meeting is used to plan a new sprint and takes place as soon as a Sprint has been completed.
Three main Questions are discussed in this meeting. These include defining a new Sprint Goal, which items from the
Product Backlog should be included in the upcoming Sprint and how an increment that meets the Definition of Done can be
created.

Sprint Review
^^^^^^^^^^^^^
During this meeting, the result of the Sprint is reviewed and adjustments are made.

Our team presents their work and progress towards the Product Goal. Based on the information, the next steps can be
planned.

Sprint Retrospective
^^^^^^^^^^^^^^^^^^^^
This meeting is very important. It is used to plan how to improve the quality and effectiveness of our work. The team
reviews how the last sprint went in terms of individual team members, interactions, processes, tools and their
Definition of Done. We discuss, what went well during the Sprint and what didn't, what problems were encountered and how
they were solved or can be solved.

Milestone Meeting
^^^^^^^^^^^^^^^^^
After each milestone there is a meeting with the Advisor. We present a small demo of our project and show
the status of the product.

Meeting Timetable
^^^^^^^^^^^^^^^^^
In the following table one can see how we have scheduled the meetings.

=====================  =================================  =======================  ========================
 Meeting Timetable     | Friday 1                         | Friday 2               | Friday 3
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

Protocolling
^^^^^^^^^^^^
For each meeting a protocol is created. These record what we discussed in the meeting, what decisions were made and any
open issues.

Risk Management
---------------


Quality Management
------------------

Requirements Engineering
************************

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

Glade
-----
For our graphical user interface (GUI) we use Glade. Glade is a rapid application development tool (RAD) and allows us
to quickly and easily develop user interfaces for the GTK toolkit

GTK
---
GTK is a free and open-source cross-platform widget toolkit. We use it to develop our Black Fennec app.



