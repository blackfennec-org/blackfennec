.. _Version Control Strategy:

Version Control Strategy
========================

This project does version control using Gitlab according to the git Workflow. Before a feature branch can be merged a merge request MUST be created.

Merge Requests
**************

There MUST always be two members of the project assigned to a merge request. An assignee who has the competence to merge and a reviewer who both are obligated to check whether the commits fulfill the :doc:`definition_of_done`. The Assignee is assigned to the "quality assurance" role, and the reviewer depends on the topic the merge request is about. In this project code mainly regarding UI is assigned to the "user experience" role, any other code to the "architecture" role. Changes solely regarding the documentation are assigned to the "documentation" role.

Approval
--------

Both assigned roles SHOULD give their approval to a merge request. The assignee however can merge without the approval of the reviewer IFF the reviewer exceeds the maximal time of one week without giving his approval and without starting a conversation.

Comments
--------

Assigned roles can, if the quality does not suffice open a communication by writing a comment. These comment must be resolved before the merge request can be merged.

Coverage
--------

The coverage in a merge request can be seen in Gitlab. A pipeline automatically uploads a coverage report created with the tool pytest. The coverage of a merge request SHOULD not lower the previously established coverage, but in some cases this cannot be hindered. But in any case the coverage SHALL never be lower than 90 Percent.

Pipelines
*********

The Gitlab pipelines of this project are to be split into separated folders to improve the overviewability, and pipeline run-times when making changes to files significant to the rebuilding of the building docker images.

Building docker images
----------------------

To improve pipeline run times a docker in docker build is done for the generation of the documentation and the testing and deployment of the project. These build images that have installed the required packages to be able to fulfill their respecting task are uploaded into the Gitlab container registry from where they are pulled for succeeding tasks.

Deployment
----------

The deployment of the project and associated extensions are uploaded into the PyPI package registry also in the Gitlab repository. From there they can be downloaded using the Python package management tool pip.
