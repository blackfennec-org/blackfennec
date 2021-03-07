Selection Process
=================
The selection process solves the problem of composing what is considered the best interpretation_ of the underlying data. We sometimes refer to this process as an auction_. The exact implementation is subject to change and this document will cover the subject in general terms.

Problem Statement
"""""""""""""""""
For reasons that don't concern, we want to find the best interpretation_ of the underlying data structure given all the known types. Types are considered known if they have been previously registered with the `type registry`_.

Conceptual Solution
"""""""""""""""""""
Conceptually speaking - meaning that this does not necessarily reflect the implementation to closely - all registered types are asked to produce a score or a bidding_ on how good they can represent the data structure. From the result of this process we decide which type will be the officially best interpretation of the data structure.


Glossary
""""""""
.. _interpretation:

interpretation
  In the context of this document an interpretation is understood to be the visual representation of the data structure.

.. _type registry:

type registry
  In the context of this document the type registry is a centralised and authoritative database of all known types. In practice some of these types may have been registered by extensions.

.. _auction:

auction
  In a real world auction objects (data structures) are sold (transfer of responsibility) to the highest bidder (type). We use this analogy to think of this process abstractly.

.. _bidding:

bidding
  A bidding is a complex score describing the willingness of the type to represent a given structure. The analogy of an auction will be used in other contexts to describe this process.