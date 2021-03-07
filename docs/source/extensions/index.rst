Extensions
==========
The capability and usability of Black Fennec is largely dependent on the available extensions. We take the division of responsibilities and the design of the interfaces serious and strive for stability and compatibility. That being said, this document and the definitions it contains are at this stage very much a work in progress and subject to change.

Three conceptual types of extensions are currently planned. Any given extension however, can include multiple of these conceptual types as well as multiple conceptual extensions of the same type.

.. uml::

    @startuml
    hide circle
    hide members
    hide methods

    title Conceptual Extension Landscape

    skinparam class {
        BackgroundColor #EEE
        ArrowColor Black
        BorderColor Black
    }

    class BlackFennec {}

    BlackFennec -> "0..*" Extension

    interface Extension {
        load(extension_api)
        unload()
    }

    note top of Extension: An extension consists of at least one of \nType, Action or Presenter Extension

    Extension -> "1" ExtensionApi

    class ExtensionApi {
        register_type(bidder, view_factory)
        register_action(type, action)
        register_presenter(description, view_factory)
    }

    abstract class TypeExtension {}
    Extension "1" o-- "0..*" TypeExtension

    abstract class ActionExtension {}
    Extension "1" o-- "0..*" ActionExtension

    abstract class PresenterExtension {}
    Extension "1" o-- "0..*" PresenterExtension
    @enduml



.. uml::

    @startsalt
    title Wireframe of Extension Types Working Together

    {+
        {* Open | Save | Extensions | About }
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
                        key2    | value2
                    }
                    {* <&bolt> Actions
                        <&bolt> Actions | <color:Red>action extension C | <color:Red>action extension D
                    }
                }
            }
        }
    }
    @endsalt

Type Extension
""""""""""""""
More can be read in the document :doc:`type_extension`

Type extensions are expected to be the most common type of extension. They enrich the object model with an additional type and its visualisation.


Action Extension
""""""""""""""""
An action extensions is capable of adding actions to the system. An action is performed in the context of an object (instance of a type) and can - and usually does - effect the structure data. Actions therefore depend on types.

Presenter Extension
"""""""""""""""""""
Presenter extensions have some control over the visualisation of the data. They are however confined to a window [#]_ and have very limited control (size and position) over the visualisation of types as this is provided by the types themselves.

Extension Api
"""""""""""""
To integrate extensions into the flow of Black Fennec, the extension api is injected at load time. This interface allows extensions to register themselves to hooks and into registries. Extensions are not treated differently, regardless of their conceptual type.


.. [#] Window: A rectangular are of the screen.