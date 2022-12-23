.. _design_decisions:

================
Design Decisions
================

This section of the documentation serves as an overview of the architecture and package-/class-design. This document serves only as an overview. More detailed
information can be found in the documents referenced in this overview.

Physical Architecture
"""""""""""""""""""""
Black Fennec is a single user application running on a single computer and does not interact with the network necessarily. The main engineering challenges in the project stem from the complexity and some of the required algorithms to implement the functionality.

Logical Architecture
""""""""""""""""""""
Black Fennec is best described as a set of services and interfaces that serve different stakeholders and allows communication between them. The main packages are described in the Architecture documentation and a detailed overview over the most important components are documented in the domain model. Each loosely coupled component solves a different problem. For example, the `Structure` abstracts data access, filtering and implements recursion via `References`.

Application and Programming Interfaces
""""""""""""""""""""""""""""""""""""""
The packages have been designed with low coupling and high cohesion in mind and exist largely independent from each other. This was necessary to manage the complexity of the project. The interfaces are weakly typed and rigorously tested as this is the pythonic way.

Persistence
"""""""""""
Since we do not have a backend or database, persistence was not a real problem which needed solving in our case. Nevertheless, serialisation of user data was implemented with the visitor pattern giving us great flexibility in the output format (JSON, YAML etc).

Package Design
""""""""""""""
We deploy a great many design patterns to manage the complexity of this project; MVVM, Abstract and Simple Factory, Visitor to name the most prominent ones. Listing them all here would be besides the point.

User Experience
"""""""""""""""
To ensure the user experience, we created a special role in the team. We started early on with design concepts and integrated UX requirements with the help of :ref:`Matthew`.
Additionally we created a usability study which is to be done for new feature included in a release. The template can be found :ref:`here <usability_test_template>`.

Architecture Highlights
"""""""""""""""""""""""
The main feat of the architecture is its capability to hide enormous complexity in simple to use services. Many of our components require significant time to understand - not because they are poorly implemented but due to the sheer complexity of the problem they are solving. But even so, using them is as simple as it gets. This allowed us to work in parallel at different aspects of the system and resulted in near seamless integrations and extensibility.


Possible Extensions
"""""""""""""""""""
Although Black Fennec is a very viable product, we have yet to deliver some of the features teased in the project proposal. The most prominent of them are `actions`. We recently decided that this feature could not be implemented within the time constraints of the engineering project. However, it is perfectly feasible to add `actions` in the future. As a matter of fact, we plan to do so.

Furthermore, Black Fennec is designed to be extended by :ref:`extensions <definition_extension>`. This allows users as well as developers to implement new functionality as they see fit. The possibilities are quite literally endless.

.. _performance_scenario:

Performance Scenario
""""""""""""""""""""
This isn't much a concern for us as Black Fennec is a single user desktop application. Our project is never used by more than one user. Anyone who wants to use Black Fennec can install the application locally on the machine and work with it. The performance bottlenecks that we see are mainly related to file size and the amount of installed extensions.

System Test
"""""""""""
Which is why we have a dedicated system test that ensures that large files (1 MB/ 100'000 lines) can be opened in under one second. This is tested each release cycle, to ensure nothing has broken this requirement.

To ensure that the second bottleneck that we have identified, namely the installation of many type plugins, each bidding on every viewed structure. For this a special extension, loading the same bidder a thousand times while opening a large files (1 MB/ 100'000 lines) was created.
