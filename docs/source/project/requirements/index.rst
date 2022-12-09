.. _requirements_engineering:

========================
Requirements Engineering
========================

In General we refrain from defining Use Cases in the requirements engineering in this project. We took a more user centered approach and focus our requirements engineering on Epics and User Stories. Additionally to the functional requirements that are specified in this user centered approach, non-functional requirements are evaluated in a separate document :doc:`non_functional`.

Additionally to the traditional requirements, wireframes of the UI were created to give the viewer an initial understanding of how the application might look like. These can be found in the document :doc:`ui_sketches`

Epic Overview
*************
This diagram provides an overview over the epics that our specified personas found under :doc:`personas` would like to be able to do with Black Fennec. It is intentionally done in the way of an UML-Diagram Overview but is apart from the format quite different. The personas are not representing specific roles that have to be able to do something but a category of users that have certain needs and expectations.

.. uml:: epic_overview.puml

User Stories
************
The user epics described in this document can be found in the github repository under the `epics label <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/boards/240?scope=all&utf8=%E2%9C%93&label_name[]=Epic>`_. These epics are broken down into more detailed parts called user stories which can only be found under the `user story label <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/boards/240?scope=all&utf8=%E2%9C%93&label_name[]=User%20Story>`_ and are not part of this documentation. User stories are created in the range of sprint plannings or a dedicated backlog-refinement meeting and the overarching epics are deleted once all contained user stories are finalised.

.. toctree::

    non_functional
    personas
    ui_sketches
