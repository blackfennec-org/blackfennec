***********************
Architecture and Design
***********************
This section of the documentation serves as an overview of the architecture and package-/class-design. This document serves only as an overview. More detailed
information can be found in the documents referenced in this overview.

Physical Architecture
=====================
Black Fennec is a single user application running on a single computer and does not interact with the network necessarily. The main engineering challenges in the project stem from the complexity and some of the required algorithms to implement the functionality.

Logical Architecture
====================
Black Fennec is best described as a set of services and interfaces that serve different stakeholders and allows communication between them. The main packages are described in the Architecture documentation and a detailed overview over the most important components are documented in the domain model. Each loosely coupled components solves a different problem. For example, the `Structure` abstracts data access, filtering and implements recursion via `References`.

Application and Programming Interfaces
======================================
The packages have been designed with low coupling high cohesion in mind and exist largely independent from each other. This was necessary to manage the complexity of the project. The interfaces are weakly typed and rigorously tested as this is the pythonic way.

Persistence
===========
Since we do not have a backend and no database, persistence was not a real problem which needed solving in our case. Nevertheless, serialisation of user date was implemented with the visitor pattern giving us great flexibility in the output format (JSON, YAML etc).

Package Design
==============
We deploy a great many design pattern to manage the complexity of this project; MVVM, Abstract and Simple Factory, Visitor to name a few. Listing them all here would be besides the point.

User Experience
===============
To ensure the user experience, we created a special role in the team. We started early on with design concepts and integrated UX requriements with the help of :ref:`Matthew`.

Architecture Highlights
=======================
The main feat of the architecture is its capability to hide enormous complexity in simple to use services. Many of our components require significant time to understand - not because they are poorly implemented but due to the sheer complexity of the problem they are solving. But even so, using them is as simple as it gets. This allowed us to work in parallel at different aspects of the system and resulted in near seamless integration and extensibility.


Possible Extensions
===================
Although Black Fennec is a very viable product, we have yet to deliver some of the features teased in the project proposal. The most prominent of them are `actions`. We recently decided that this feature could not be implemented within the time constraints of the engineering project. However, it is perfectly feasible to add `actions` in the future. As a matter of fact, we plan to do so.

Furthermore, Black Fennec is designed to be extended by :ref:`extensions <definition_extension>`. This allows users as well as developers to implement new functionality as they see fit. The possibilities are quite literally endless.

Performance Scenario
====================
This isn't much a concern for us as Black Fennec is a single user desktop application. Our project is never used by more than one user. Anyone who wants to use black fennec can install the application locally on the machine and work with it. The performance bottlenecks that we see are mainly related to file size and the amount of installed extensions. However, in all our tests we never experienced any performance issues.

Technologies Used
=================
Black Fennec is a Python based GTK3 application. We have mastered both technologies. To be fair, our engineering challenges were not really created through the use of technology and could not have been solved significantly better in other programming languages. 