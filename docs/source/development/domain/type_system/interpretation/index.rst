.. _interpretation_service:
.. _interpretation:
.. _definition_selection_process:

==============
Interpretation
==============

The process of interpretation solves the problem of composing what is considered the best interpretation of the underlying data. We sometimes refer to this process as an auction. Its exact implementation is subject to change and this document will cover the topic in general terms.

On of the main features of Black Fennec is to find the best interpretation of a given :ref:`Structure <definition_structure>` using known :ref:`Types <definition_type>`. Types are considered known if they have been previously registered with the :ref:`Type Registry <type_registry>`.

Conceptually speaking - meaning that the following is not how we actually do it but how you can imagine it works - all registered types could be asked to produce a score (sometimes referred to as an offer) on how good they can represent the data structure. From the result of this process we decide which type will officially be the best interpretation of the data structure. The simplest possible implementation of this process would use a boolean as the score and select the first type that scores ``true``.

.. _definition_interpretation_service:

Interpretation Service
======================
The interpretation process is implemented in the Interpretation Service which in turn creates Interpretations. To create an Interpretation the Interpretation Service must evaluate and sort all known Types. The resulting sorted list of Types is then included in the Interpretation along with some metadata.

.. uml:: interpretation_sequence.puml

The caller of the Interpretation Service often uses the interpretation to later display the structure. Other use cases include the filtering of :ref:`Actions <definition_action>` based on the Interpretation.


.. _definition_interpretation:

Interpretation
==============
The interpretation contains an ordered list of types associated with a structure. An interpretation created through the interpretation service is what Black Fennec believes to be the best available representation of a given structure.
