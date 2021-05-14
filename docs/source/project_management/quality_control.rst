***************
Quality Control
***************
This document gives an overview over the quality control measures taken in this project. We will reference dedicated documents which are considered single-source-of-truth on their respective topics and we recommend reading them for a better grasp of all active policies.

Planning and Reviews
====================
Quality has been one of our top concerns from the get-go and we have planned for it accordingly. We deploy multiple techniques to ensure the quality of our product - including its documentation.

One of the first artifacts produced was our :ref:`quality assurance <Quality Assurance>`, in which we outlay in detail the measures we take to ensure the high quality we require.

Documentation
-------------
Changes to the documentation are handled like any other changes to any other artefact with the addition of work items specifically to ensure consistency and relevance. We utilise our usual review processes to ensure correctness and the communication of knowledge. This entails the inclusion of the work done in sprint reviews and retrospectives as outlined in our :ref:`definition of scrum <Definition of Scrum>`. The results of these meetings is documented in gitlab issues such as <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/issues/114> and <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/issues/93>.

Code Reviews
------------
As previouly mentioned, we deploy multiple measures to ensure the quality of the project. This includes code reviews. Our workflow is heavily inspired by the gitflow work flow as documented in our :ref:`version control strategy <Version Control Strategy>` and includes `merge requests`. Each merge request is reviews by at least one other developer to not only ensure quality but also spread domain knowledge as evenly as possible. Additionally we deploy automated reviews and enforce `code style guidelines` with the help of `pylint` as documented in :ref:`code style guidelines <Code Style Guidelines>`.

Testing
=======
Stability and regression safety are at the forefront of quality control. This is precisely why we uphold very high testing standards in this project. Our test coverage is constantly around 94% and we encourage our developers to take the time to achieve 100% coverage for non-UI code. To ensure that all tests are passed before merging with the `dev` or `master` branch, we configured `gitlab` in a way to strictly disallow this.

If you are interested in the documentation of coverage and failed pipelines, we suggest visiting the gitlab built in analytics for `pipelines <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/pipelines/charts>`_ and `coverage <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/graphs/dev/charts>`_.


Unit Tests
----------
In the `tests` directory it is possible to find over 600 unit tests which try to ensure the correctness of single components. We deploy a multitude of doubles including mocks, fakes and stubs which can be found in the `doubles` directory.

Integration Tests
-----------------
Fewer in number but equally important are our integrations tests. These tests ensure that the components tested with unit tests also work together.

System Tests
------------
The highest level of testing we conduct are system tests. As they are time consuming in their execution, we restrain from utilising this tool for every merge request. However we do execute them before publishing a new release. The templates can found :ref:`here <System Test Templates>` and the protocols :ref:`here <System Tests>`.

Tools for Quality Control
=========================
As mentioned before, we have integrated tools in our continuous integration work flows. The tool `pylint` is in fact highly configurable and includes every metric in the book.

Additional Measures
===================
Besides functional requirements we also test non-functional requirements in our System Tests, including performance and usability tests. However the subject of performance was not one of our main concerns as we develop a single user desktop application. Usability on the other hand was addressed with the creation of a dedicated role in the team and even a persona named :ref:`Matthew`. Early and interactive UI sketches also guided and accelerated the process. Additionally, we developed a :ref:`definition of done <Definition of Done>`, :ref:`logging standards <Logging Standards>` and :ref:`corporate identity & design <Corporate Identity & Design>`.