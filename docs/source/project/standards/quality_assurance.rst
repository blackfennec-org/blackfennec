.. _quality_assurance:

Quality Assurance
=================
To ensure the desired quality in this project many different standards are enforced.

Produced Artifacts
""""""""""""""""""
All created artifacts of this project are contained within the project Gitlab repository to which any associated person has access. This ensures that of every file a detailed change history is available. For a detailed elaboration on our Version Control Strategy a dedicated document :ref:`version control strategy <version_control_strategy>` exists.

Documentation
"""""""""""""
Our documentation is written in the Markdown-flavour RestructuredText and is version controlled in Gitlab. The generation and provision of the Documentation is automated through a CI-Pipeline task and is automatically built when attaching a tag to a commit. The documentation also is a project artifact and therefore also falls under the :ref:`version control strategy <version_control_strategy>`.

Documentation Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^

Changes to the documentation are handled like any other changes to any other artifact with the addition of work items specifically to ensure consistency and relevance. We utilise our usual review processes to ensure correctness and the communication of knowledge. This entails the inclusion of the work done in sprint reviews and retrospectives as outlined in our :ref:`definition of scrum <definition_of_scrum>`.

The Language used in the documentation of this project is english. Created it is with the Sphinx framework and RestructuredText. Before a commit the developer has to build the document on his local system to ensure the build passes successfully. For this a makefile is provided which can be executed with make docs.

The documentation is written with the form follows function principle in mind. The software as a product is the main goal of this project and a functional documentation can be written more efficiently.

Project Management
""""""""""""""""""
Project Management is done with Gitlab as well. The Issue-Boards are used in this project to represent our different steps an issue can undergo. The ordering in the lists show the importance of each issue. The higher up an issue is, the higher is its importance. The issues created can be assigned to members of the team and to the milestone that they belong to. To know to which sprint an issue is associated with, dedicated Sprint labels are created at the start of a sprint.

The different steps an issue can undergo are described in the following table.

================  ====================
Column (Label)    Description
================  ====================
Roles             These issues represent different roles in which administrative effort can be captured.
Draft             The drafted issues are in a pre-stage before making it into the backlog. Here any member can enter ideas that come up during sprints and are then evaluated by the Product Owner
Backlog           Only the Product Owner is allowed to define the Backlog. Here Definite Tasks that are going to be implemented are listed.
Sprint Backlog    This Column is the Backlog for the Sprint and requires the items to be actual user-stories and on a Work-item level so that one person can be assigned to this task.
In Progress       In this list are issues that are in progress in the current sprint.
Resolved          When an issue is resolved, this means that it adheres to the :ref:`definition of done <definition_of_done>` but was not merged yet.
Open              The Open Issue list is not used in our project as open issues tend to reside in dedicated lists.
Closed            When an feature was successfully merged its issues move to the list closed where all past issues reside.
================  ====================

Development
"""""""""""
Procedure
^^^^^^^^^
As previously mentioned all our artifacts including our code is contained in Gitlab. For any versioning specific practices one can look into the :ref:`version control strategy <version_control_strategy>`. In there the handling of merge requests is explained. This ensures a dual control principle regarding not only logic errors but also formatting and code style.

Additionally to the dual control principle our Gitlab pipelines have built in execution for testing and linting.

.. _code_style_guidelines:

Code Style Guidelines
^^^^^^^^^^^^^^^^^^^^^
To support well-formatted coding, every team member is required to install pylint, a linting tool that not only can  enforce Coding Standards according to Pythons PEP8 style guide but also features an error detection and refactoring help. Additionally a pipeline task that includes pylint checking is included in the ci on Gitlab. A Script is used to convert the pylint error codes into a rating, preventing the task to fail from notices other than errors. The .pylintrc file is copied from the `Google Styleguide <https://github.com/google/styleguide/blob/gh-pages/pyguide.md>`_. But it is intended to update the pylintrc configuration file to exclude warning generating rules, if the whole team approves.

Code Reviews
^^^^^^^^^^^^

Our workflow is heavily inspired by the gitflow work-flow as documented in our :ref:`version control strategy <version_control_strategy>` and includes `merge requests`. Each merge request is reviewed by at least one other developer to not only ensure quality but also spread domain knowledge as evenly as possible. The assignee and reviewer additionally should read the code and try to understand it, and if unclear ask the creator.

Additionally, we deploy automated reviews and enforce `code style guidelines <code_style_guidelines>` with the help of `pylint`.


Pair Programming
^^^^^^^^^^^^^^^^
An important tool in our project will be the use of pair programming. It will not be done for every function that is written but if anyone is stuck and is only progressing slowly this shall be recognized during our daily Scrum meetings and another member of the team will try to help resolve the problem with a fresh mind.

Testing
"""""""

Stability and regression safety is at the forefront of quality control. This is precisely why we uphold very high testing standards in this project. We encourage our developers to take the time to achieve 100% coverage for non-UI code. To ensure our high standards we configured our CI/CD pipeline to strictly require a branch coverage of 90% or more as well as the passing of all available tests. As a result our test coverage is constantly around 94%. 

If you are interested in the documentation of coverage and failed pipelines, we suggest visiting the gitlab built-in analytics for `pipelines <https://gitlab.ost.ch/blackfennec/blackfennec/-/pipelines/charts>`_ and `coverage <https://gitlab.ost.ch/blackfennec/blackfennec/-/graphs/dev/charts>`_.

The tests are stored in a separate location in the tests folder. There each python file of our application that is tested has a corresponding testing file that preferably has the same name if no ambiguities are present.

A doubles folder exists where commonly used doubles a saved in specific files separated by component they belong to.

Unit Testing
^^^^^^^^^^^^
Unit tests are done with the pytest framework in our project. We value test-driven-development and strive for 90% of testing coverage. Every developer is ought to have pytest installed in his development environment and additionally a pipeline ensures that all tests are always passing. A merge request without passing pipelines is prohibited from being merged.

Integration Testing
^^^^^^^^^^^^^^^^^^^

Fewer in number but equally important are our integrations tests. These tests ensure that the components tested with unit tests also work together.

Integration Tests are done in the PyTest framework as well. They reside in separate files with an \"_integration\" addition to their filename and should be marked as integration tests with the pytest decorator `@pytest.mark.integration`. Since the integration tests are mostly contained in separate files, it is also possible to mark the whole file with `pytestmark = pytest.mark.integration`.

System Tests
^^^^^^^^^^^^
To ensure the integrity of the system as a whole, we conduct system tests before releasing a new version. We restrain from executing the system test suit for every merge request, because they are very time consuming and cover most aspects of the applications normal execution, most of which are likely to remain unchanged. As a replacement we relay on manual, undocumented tests done by the developer and reviewer.

Since the System Tests are not automated, they are written down in a specific test protocol that is created using the :ref:`system test template <System Test Templates>`. This way the tests can be done multiple times using the same template. As with the documentation of the project it is expected to append the test protocol when adding new functionality.

The protocols are contained in a single file that can be found :ref:`here <System Tests>`. This file includes all recent releases and their respective test protocols.

Usability Tests
^^^^^^^^^^^^^^^
On top of all the functional testing conducted as described above, we also undertake usability studies. These tests are usually performed at the end of a project with the goal of having each :ref:`persona <personas>` represented by at least one participant. The templates can found :ref:`here <usability_test_template>` and the protocols :ref:`here <usability_study>`.
