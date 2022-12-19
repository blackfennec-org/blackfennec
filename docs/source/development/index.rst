.. _development:

===========
Development
===========

Black Fennec is, in essence, a glorified JSON viewer with a powerful extension API. Extensions can add custom types, views, actions and even new mime types. As such this documentation caters to two types of developers.

The goal of Black Fennec development is to ensure the stability, extensibility and usability of the software. This is achieved by following a set of standards and best practices which are described in :ref:`project standards <project_standards>`. As a developer you should be aware of these standards. However, it is also important to understand the bigger picture, the architecture and the domain model. This is explained in :ref:`architecture <architecture>` and :ref:`domain model <domain_model>` respectively.

Extension developers make Black Fennec more then just a glorified JSON viewer. The available extensions largely determine the usefulness of Black Fennec. Thus a :ref:`dedicated section <definition_extension>` explains how to write the different types of extensions.

In the :ref:`testing <testing>` section we record and document system and usability tests.

Finally, the :ref:`code <code_documentation>` section contains a generated source code documentation of Black Fennec.

.. toctree::
    :maxdepth: 2

    architecture/index
    domain/index
    extensions/index
    testing/index
    code
