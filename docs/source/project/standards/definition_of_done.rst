.. _definition_of_done:

Definition of Done
==================
For each work item an issue MUST be created. An issue is considered done IFF it's corresponding commits have been successfully merged into the dev branch. Furthermore, the time spent MUST be documented.

Merging into dev Branch
***********************
A merge request MUST be created for merging into the dev branch.

| Before any such request can be accepted,
| merge requests MUST:

* passing of pipeline
* test coverage is above 90 percent
* be reviewed by another developer
* have all conversations resolved

Merge requests SHOULD:

* NOT lower test coverage
* confirm to the projects :doc:`logging_standards`
