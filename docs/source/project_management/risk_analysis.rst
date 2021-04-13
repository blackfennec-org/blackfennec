Risk Analysis
=============
.. _risk_analysis:

This document contains a list of all identified technical risks to the Black Fennec engineering project. It is updated on a need be basis.

Reaching the Complexity Ceiling
"""""""""""""""""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ================  ==========
    **Damage**        Very High
    **Probability**   1.0
    **Danger**        Very High
    ================  ==========


The project is to complicated or complex for developers to effectively make changes or add features.

Mitigation
^^^^^^^^^^
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Reduce  
    **Effectiveness**   0.5           
    **Remaining Risk**  Medium
    ==================  ===========

Managing complexity effectively is very hard. We must deploy many techniques and tools to mitigate this risk effectively. We will invest heavily into the architecture of the system and additionally strive for flexibility for when simpler solution arise they may be implemented. Flexibility through refactoring is aided by unit tests, giving the developers confidence in rapid changes.

The remaining risk must be watched carefully and further analysis will take place before the issue raises to dangerous levels.

Changing Requirements
"""""""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Damage**          Medium  
    **Probability**     0.6           
    **Danger**          Low
    ==================  ===========

The critical requirements change or can not be satisfied, arising the need to rewrite large parts of the project.

Mitigation
^^^^^^^^^^

.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Avoid  
    **Effectiveness**   0.5           
    **Remaining Risk**  Very Low
    ==================  ===========

Since we are in control of the requirements for our product we will try not to change them in any breaking way. Additionally, we have already analysed the requirements on a higher level and believe them to be manageable.

Documentation Tools
"""""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ================ =========
    **Damage**       Medium
    **Probability**  0.2     
    **Danger**       Very Low
    ================ =========

The tools used to document the project are inadequate for the documentation of this project.

Mitigation
^^^^^^^^^^
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Retain  
    **Effectiveness**   0.0
    **Remaining Risk**  Very Low
    ==================  ===========

We have decided to use the recommended documentation tool. We believe it to be adequate. However if it turns out to be inadequate we decided to work around that issue or in other words accept the limitations and work within them.

Development Tools
"""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Damage**          Very Low  
    **Probability**     0.3           
    **Danger**          Very Low
    ==================  ===========

The chosen IDE, VCS etc does not support the development process

Mitigation
^^^^^^^^^^
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Reduce  
    **Effectiveness**   0.8           
    **Remaining Risk**  Very Low
    ==================  ===========

We will set the project up in a way that these factors cannot effect us in any significant way. In fact some developers will be using different IDEs. 

Third Party Component
"""""""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Damage**          High  
    **Probability**     0.8           
    **Danger**          High
    ==================  ===========

A third party component is limited, damaged or otherwise unsuited for our purposes. This includes bugs as well as security vulnerabilities.

Mitigation
^^^^^^^^^^
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Reduce  
    **Effectiveness**   0.68 [#]_
    **Remaining Risk**  Medium
    ==================  ===========

We will evaluate all used third party components before settling with the best match. Additionally, we will abstract the dependency as good as possible with patterns like Repository Pattern and MVVM. This results in significant protection against this risk but cannot mitigate all dangers. 

The remaining risk is retained.

Low Software Quality
""""""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Damage**          Medium  
    **Probability**     0.8           
    **Danger**          Medium
    ==================  ===========

The quality of the software hinders development, maintainability or adaptability. This will long term reduce the relevance of the project.

The reason why we categorise the damage as "medium" stems from the assumption that this risk would materialise towards the end of the engineering project. At this point we hope to have implemented most important user stories relevant to the project. If however the project would be continued over an extended period of time the damage would could may as well be fatal.


Mitigation
^^^^^^^^^^
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Reduce  
    **Effectiveness**   0.5
    **Remaining Risk**  Low
    ==================  ===========

Regular refactoring and a strict and rigorous quality control process is hoped to ensure the quality of the software. Besides policies and processes, effective testing should allow us to refactor with more confidence and therefore more often. Furthermore, as mentioned in `Reaching the Complexity Ceiling`_, we will invest into the architecture as we believe that good design and the reduction in complexity will be reflected in the overall quality.

Bad User Experience
"""""""""""""""""""
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ===============  ===============
    **Damage**       High  
    **Probability**  0.8           
    **Danger**       High
    ===============  ===============

The product does not satisfy the users or customers, resulting in low adoption and - if not mitigated - ends in the death of the project.

This is a rather long term threat to the project but still one that we take very seriously. As we work in a admittedly complicated domain, it is as crucial as it is complicated to achieve good UX.


Mitigation
^^^^^^^^^^
.. table::
    :widths: auto
    :align: left
    :class: borderless

    ==================  ===========
    **Strategy**        Reduce  
    **Effectiveness**   0.68
    **Remaining Risk**  Medium
    ==================  ===========

We have created the role "user experience" and dedicated a member of our team towards the goal of ensuring the usability of our product. We are not confident enough in this mitigation strategy to retain the risk at this point. However, at this point in the project we do not have enough information to decide on further mitigation strategies. Therefore, this risk must be looked out for.

Footnotes
"""""""""

.. [#] An experience value denoting significant chance