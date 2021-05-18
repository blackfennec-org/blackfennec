.. _presenter:
.. _definition_presenter:
.. _presenter_extension:

Presenter Extension
===================
The presenter extension (a.k.a Info Presenter Extension) is responsible for displaying and positioning all Info Views as described in :doc:`type_extension` as well as making Actions as described in :doc:`action_extension` available to the user. Presenters have few restrictions and will be given a rectangular area for rendering.

.. uml::

    @startsalt
    title Wireframe of a Graph Based Presenter

    {
        <color:Red>presenter extension E
        {S
            {+<color:Red>type extension A
                {+
                    key1    | value1
                    key2    | value2
                    key3    | ->
                }
            } | {
                .
                ---------
                .       I
                .       I
                .      V
            } | { .
                {+<color:Red>type extension C
                    {+
                        key1    | value1
                    }
                }
                .      ^
                .       I
            }
            . | {+<color:Red>type extension B
                {+
                    key1    | ->
                    key2    | ->
                }
                {* <&bolt> Actions
                    <&bolt> Actions | <color:Red>action extension D | <color:Red>action extension E
                }
            } | {
                .       I
                ---------
                .       I
                .       I
                .      V
            } 
            . | . | {+<color:Red>type extension C
                {+
                    key1    | value1
                    key2    | value2
                    key3    | value3
                    key4    | value4
                    key5    | value5
                }
            }
        }
    }
    @endsalt

.. uml::

    @startsalt
    title Wireframe of a Column Based Presenter
    {
        <color:Red>presenter extension E
        {S
            {+<color:Red>type extension A
                {+
                    key1    | value1
                    key2    | value2
                    <b>key3 | <selected>
                }
            } | {+<color:Red>type extension B
                {+
                    key1    | value1
                    <b>key2 | <selected>
                }
                {* <&bolt> Actions
                    <&bolt> Actions | <color:Red>action extension C | <color:Red>action extension D
                }
            } | {+<color:Red>type extension C
                {+
                    key1    | value1
                    key2    | value2
                    key3    | value3
                    key4    | value4
                    key5    | value5
                }
            }
        }
    }
    @endsalt


Displaying Info Views
"""""""""""""""""""""
Info Views are placed and positioned by the presenter. They ought to expect a rectangular region in which they are allowed to render information. The presenter has full control over size and position of these regions and is free to arrange and decorate them. It is not the responsibility of the presenter to ensure the usability of the Info View. However, we might define a soft limit to the minimum width or height that a Info View ought to get.

Disclaimer
""""""""""
At this point we do NOT plan on implementing more than one presenter.