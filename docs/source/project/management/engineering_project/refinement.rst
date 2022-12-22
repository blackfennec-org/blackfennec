.. _refinement:

==========
Refinement
==========

After each sprint, a review meeting was held to discuss the current status of the project. The checklist of the individual milestones was discussed and it was ensured that all items on the list were fulfilled. During the meetings, we received some suggestions for improvement from our supervisor, which we implemented during the course of the project.

This document provides an overview of all these improvement suggestions and how they were implemented in our project.

Project Plan
""""""""""""

Improvements
------------

**Role Project Lead / Project Manager must be added in the documentation**
The description of this role was added in the document project plan under :ref:`project manager <project_manager>`.

**Rough plan of the project must be created and added in the documentation**
We created a project timeline in the document :ref:`project timeline <project_timeline>`

**Add the time needed to respond to the risk to the risk analysis and the rough plan of the project**
The time needed to respond to a risk is included in the :ref:`project timeline <project_timeline>` by the use of phase buffers but do not address specific risk but rather correspond with when risks are most likely to occur.

Requirements Engineering & Domain Analysis
""""""""""""""""""""""""""""""""""""""""""

Improvements
------------

**Use the personas in the use-cases**
We did this by relating the user stories to specific personas. An example of this can be found in the following issue (issue does not exist anymore).

**Add sketches from extensions as soon as they exist**
These sketches were added in the form of wireframes to the domain model document.


Architecture Prototype & End of Elaboration
"""""""""""""""""""""""""""""""""""""""""""

Improvements
------------

**It is hard to make a connection between the architecture documentation and our structure in the code. We should therefore consider either adapting the documentation or the folder structure**
With a major refactoring of the structure we ensured that the architecture documentation matches the structure of the code. For more details on this refactoring one can look at following issue (issue does not exist anymore).

Software Architecture
"""""""""""""""""""""

Improvements
------------

**Consider adding a performance test. E.g. insertion of large files**
Performance tests were added at the two identified bottlenecks that our application has and are now included in the system tests performed before each release. For more information look at the :ref:`performance scenario <performance_scenario>` chapter.

**The document contains only static views of the system. Consider adding a dynamic view of the system**
Multiple dynamic views in the form of three sequential diagrams were added to the documentation.

Quality Ensurance Measurements & Code Quality
"""""""""""""""""""""""""""""""""""""""""""""

Improvements
------------

**Consider adding usability tests**
A :ref:`usability study <usability_study_v0_6>` was conducted with the participation of four completely uninvolved people, which we selected on the basis of the :ref:`personas <personas>` we created.
