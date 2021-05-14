***********************
Architecture and Design
***********************
This section of the document serves as an overview of the progress made during architecture and
package-/class-design. This document serves only as an overview of the phase. More detailed
information can be found in the :doc:`./documentation/architecture` documentation.

Physical and Logical Architecture
=================================
The architecture is quite difficult to understand. Therefore it is advisable to read the detailed description.
More can be found at :doc:`./documentation/architecture`.

Application and Programming Interfaces
======================================

Persistence
===========

Package Design
==============


User Experience
===============
To ensure the user experience, we have chosen a simple and clear design. More information about that can be found under :doc:`./requirements_engineering/ui_sketches`.
Another feature we have implemented are templates. These make it easier for a user to, for example, use their own images or lists in the tool.

Architecture Highlights
=======================


Expansion Scenario
==================
The Black Fennec project is based on a so-called base architecture. To extend Black Fennec, we decided to program extensions. This is very useful, because other users of the tool can create their own extensions and extend Black Fennec easily.

Performance Scenario
====================
Our project is never used by more than one user. Anyone who wants to use black fennec can install the tool locally on the machine and work with it. Since there is no server or anything like that in the background that the users have to connect to, this is not a problem for us.