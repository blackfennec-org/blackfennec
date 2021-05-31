.. _develop_type_extension:

Develop a Type Extension
========================
Developing a :ref:`Type extension <type_extension>` is depending on the complexity of your goals rather easy. When only a Type should be created that has some fields and you require a specialised layout for your type, this walk-through should suffice your needs, and no further reading of the domain-model is needed.

As a basis for this walk-through on how to develop a :ref:`Type extension <type_extension>` we will take one of the :ref:`base types <definition_base_types>` of black-fennec called the 'address'. To read this section it might make sense to open the projects repository located at `here <https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec/-/tree/master/src/type_system/base>`_. This allows you to individually explore the code lying behind the 'base extension' which contains the type 'address' as one of multiple types.

.. hint:: The structure that is present in this type is how black-fennec recommends an extension should be structured. But as previously mentioned this is up to the developer of the extension.

<extension_name>_extension.py
"""""""""""""""""""""""""""""

In this file the 'create_extension' and 'load_extension' functions are defined. If the function of these two functions is unclear please refer to this :ref:`document <definition_extension_development>`.

.. code-block:: python
    :linenos:

    def create_extension(extension_api: ExtensionApi):
        extension_api.type_registry.register_type(AddressBidder())

    def destroy_extension(extension_api: ExtensionApi):
        # Hint: Only the Type is passed as this static-method has no access to the created instance of 'create_extension'
        extension_api.type_registry.deregister_type(AddressBidder)

As you can see the extension_api that is passed can be used to register our type into the :ref:`type registry <definition_type_registry>`. Through the type registry it is then possible for black-fennec to use our created type in its structure :ref:`auctions <definition_selection_process>`.

.. _type.py:

<type_name>.py
""""""""""""""
This class is used by our base-extension as a helper class and represents the type which is overlayed over a Map, which is the actual underlying core type. The properties introduced are later on used for example in the view model for easier access, than always requiring to work with the underlay.


.. code-block:: python
    :linenos:

    # this address template is passed to the offer created by the bidder.
    # The offer requires this to evaluate how well your type can cover
    # a subject of the auction
    def create_address_template():
        """Address Template
        Defines the format of the address
        """
        template_map = Map()
        template_map[Address.FIRST_NAME_KEY] = String()
        # ...

        template_factory = TemplateFactoryVisitor()
        # with the appliance of the template factory your structure
        # that before was only core types.
        template = template_map.accept(template_factory)

        # after the conversion one now could make fields optional by using the following
        # syntax: template[Address.FIRST_NAME_KEY].optional = True. Per default all types
        # are required.
        return template


    class Address:
        """Address BaseType Class

        Helper class used by the address view_model representing
        the actual type 'Address'.
        Can be used by other classes as a helper to be able to
        include addresses in a overlaying datatype.
        """

        TEMPLATE = None
        FIRST_NAME_KEY = 'first_name'
        # ...

        def __init__(self, map_interpretation: Map = Map()):
            """Address Constructor

            Args:
                map_interpretation (Map): underlying map interpretation to
                    which property calls are dispatched
            """
            self._data: Map = map_interpretation
            # Initialise data structure to always contain a string
            if Address.FIRST_NAME_KEY not in self._data:
                self._data[Address.FIRST_NAME_KEY] = String()
            # ...

        @property
        def first_name(self) -> str:
            return self._data[Address.FIRST_NAME_KEY]

        @first_name.setter
        def first_name(self, value: str):
            self._data[Address.FIRST_NAME_KEY].value = value

        # ...

    Address.TEMPLATE = create_address_template()


<type_name>_bidder.py
"""""""""""""""""""""

The bidder is the component of your type extension that is asked for an offer on how well your type can handle a core type structure. The 'bid' function that takes one parameter, which contains the structure that is auctioned, has to be present in this form. As a return value an offer is expected.

.. code-block:: python
    :linenos:

    logger = logging.getLogger(__name__)


    class AddressBidder:
        """The bidding service for the base type `Address`.
        """

        def bid(self, subject: Info):
            """"Produces an offer for a given object.

            Args:
                subject (Info): The Structure for which an
                    offer should be produced.

            Returns:
                Offer: Offer that this type offers for
                    the received subject.
            """
            logger.info('bidding on object')
            return Offer(subject, 1, Address.TEMPLATE, AddressViewFactory())

The offer has 4 arguments. The first is the subject that is being auctioned. Next is the specificity of your type. Core types have the specificity of zero, and since we are directly 'inheriting by composition' from a core type our type is of specificity one. The Template is defined in the :ref:`helper type class <type.py>`. The last argument is described directly in the next chapter.

<type_name>_view_factory.py
"""""""""""""""""""""""""""
The Code of this class is quite self-explanatory thanks to the docstrings used.

.. code-block::
    :linenos:

    class AddressViewFactory:
        """Creator of the AddressView"""

        def satisfies(self, specification: Specification) -> bool:
            """Test if this view factory can satisfy the specification

            Args:
                specification (Specification): the specification to be satisfied

            Returns:
                bool: True if the specification can be satisfied. Otherwise False.
            """
            return not specification.is_request_for_preview

        def create(self, interpretation: Interpretation,
                _: Specification) -> AddressView:
            """creates an AddressView

            Args:
                interpretation (Interpretation): The overarching
                    interpretation.
                _ (Specification): The specification which can fine
                    tune the creation function.

            Returns:
                AddressView
            """
            view_model = AddressViewModel(interpretation)
            return AddressView(view_model)

The only thing left to mention are that these two functions are expected to be present in the property view_factory of the offer that your type_bidder created.

The specification is a possibility for black-fennec components or presenters to specify preferences. Until now only the distinction between whether a view created is a preview or a view is supported, but this functionality will enhance to also contain preferred dimensions, visualisation types or anything else you can imagine, as it can be handled independently when writing your own presenter.

<type_name>_view.py & <type_name>_view_model.py
"""""""""""""""""""""""""""""""""""""""""""""""

These two files depend on how one wants to visualise his type. Important is that your view is as responsive as possible, as you never know how big a presenter will show your type view. These files can also be combined into one if one refrains from using MVVM.