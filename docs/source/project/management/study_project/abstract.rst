========
Abstract
========

Introduction
""""""""""""

Black Fennec is a simple and easy to use application for viewing and editing semi-structured data like JSON in a visually interpreted form. The target audience are people that come in contact with such data on a regular basis and want to collect and manage it in an accessible way. As such it is positioned between Microsoft Word and Access and can be understood as a just-in-time form generator or data store client.

The development started in the engineering project by Lara Gubler, Leonie Däullary, Simon Kindhauser, Caspar Martens, and Thomas Kälin as supervisor. The result of which is depicted in screenshot labeled with "version 0.6".

The goal of this project was to release Black Fennec as a stable and mature product with major quality of life improvements that potential users are keen to use.

.. figure:: screenshots/blackfennec_v0.6.jpg
    :alt: BlackFennec v0.6

    State of the application before the project at version 0.6.

Approach / Technology
"""""""""""""""""""""

Improving the stability of the application included major refactorings to many components of the application. Architecture wise some of the most significant changes were made to the document subsystem, extension handling and the type system. This was made possible by a extensive and largely pre-existing automated test suite.

The test suite itself also received a major overhaul. The old suite that was using the python unittest package was largely extended and simplified through the use of the pytest framework for which the developers took part in a multi-day workshop by one of the core maintainers of pytest. More than a thousand tests cover over 98 % of the code base (branch coverage).

Thanks to the migration to GTK 4 and the use of libadwaita, the application integrates seamlessly into the GNOME desktop environment. It also improves the maintainability by providing a large set of components that are responsive and user friendly by design. Additionally the application provides better feedback, including error handling, which greatly improves user experience.

With the introduction of actions we have also introduced a new way of interacting with the application. Actions are a way of defining a set of operations that can be performed on a data structure. Overall, the extension ecosystem has matured and now offers a smorgasbord of extension points.

As means of distribution, the application is now available as a flatpak package on Flathub. This allows for easy installation and updates on all major Linux distributions. Additionally it provides a sandboxed environment that is more secure and less prone to breakage.

.. figure:: screenshots/gnome_software.jpg
    :alt: Black Fennec in the GNOME Software Center.

    Gnome software store with Black Fennec. The application is available via Flathub and thus any Linux distribution.

Result
""""""

We are happy to announce that Black Fennec is now available as a stable and mature product. The application is available on Flathub and can be installed on virtually any Linux distribution. Complementary to the release of the application, we also published a simplistic website with all relevant information including a short description, a screenshot and links to all relevant resources.

The website is available at https://blackfennec.org.

.. figure:: screenshots/blackfennec_v0.10.png
    :alt: BlackFennec v1.0

    Final release of Black Fennec at version 1.0.
