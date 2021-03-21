.. _definition_selection_process:

Selection Process
=================
The selection process solves the problem of composing what is considered the best interpretation of the underlying data. We sometimes refer to this process as an auction_. Its exact implementation is subject to change and this document will cover the topic in general terms.

Problem Statement
"""""""""""""""""
For reasons that don't concern, we want to find the best interpretation of a given structure using known types. Types are considered known if they have been previously registered with the `type registry`_.

Conceptual Solution
"""""""""""""""""""
Conceptually speaking - meaning that the following is not how we actually do it but how you can imagine it works - all registered types could be asked to produce a score (sometimes referred to as a bidding_) on how good they can represent the data structure. From the result of this process we decide which type will officially be the best interpretation of the data structure. The simplest possible implementation of this process would use a boolean as the score and select the first type that scores ``true``.

Glossary
""""""""
interpretation
  In the context of this document an interpretation is understood to be the visual representation of the data structure. The document :ref:`definition_interpretation` covers this concept.

.. _type registry:

type registry
  In the context of this document the type registry is a centralised and authoritative database of all known types. In practice some of these types may have been registered by extensions.

.. _auction:

auction
  In a real world auction objects (data structures) are sold (transfer of responsibility) to the highest bidder (type). We use this analogy to think of this process abstractly.

.. _bidding:

bidding
  A bidding is a complex score describing the willingness of the type to represent a given structure. The analogy of an auction will be used in other contexts to describe this process.