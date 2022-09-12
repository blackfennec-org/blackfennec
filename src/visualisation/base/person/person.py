# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
# from src.base.types.date import Date
from src.black_fennec.structure.template.template_factory import TemplateFactory
from src.visualisation.base.address.address import Address, create_address_template
from src.visualisation.base.image.image import Image, create_image_template

logger = logging.getLogger(__name__)


def create_person_template():
    """Person Template
    Defines the format of the person
    """
    tf = TemplateFactory()
    template = tf.create_map()

    template.add_property(
        Person.COURTESY_TITLE_KEY, tf.create_string(), is_required=False)
    template.add_property(
        Person.FIRST_NAME_KEY, tf.create_string())
    template.add_property(
        Person.MIDDLE_NAME_KEY, tf.create_string(), is_required=False)
    template.add_property(
        Person.LAST_NAME_KEY, tf.create_string())
    template.add_property(
        Person.PERSONAL_PHOTO_KEY, create_image_template(), is_required=False)
    template.add_property(
        Person.HOME_ADDRESS_KEY, create_address_template(), is_required=False)
    template.add_property(
        Person.SUFFIX_KEY, tf.create_string(), is_required=False)
    template.add_property(
        Person.GENDER_KEY, tf.create_string(), is_required=False)
    template.add_property(
        Person.SEX_KEY, tf.create_string(), is_required=False)
    template.add_property(
        Person.MARITAL_STATUS_KEY, tf.create_string(), is_required=False)
    template.add_property(
        Person.NATIONALITY_KEY, tf.create_string(), is_required=False)

    return template


class Person:
    """Person BaseType Class

    Helper class used by the person view_model representing
    the actual type 'Person'.
    Can be used by other classes as a helper to be able to
    include persons in a overlaying datatype.
    """
    TEMPLATE = None
    COURTESY_TITLE_KEY = 'courtesy_title'
    FIRST_NAME_KEY = 'first_name'
    MIDDLE_NAME_KEY = 'middle_name'
    LAST_NAME_KEY = 'last_name'
    SUFFIX_KEY = 'suffix'
    PERSONAL_PHOTO_KEY = 'personal_photo'
    HOME_ADDRESS_KEY = 'home_address'
    GENDER_KEY = 'gender'
    SEX_KEY = 'sex'
    MARITAL_STATUS_KEY = 'marital_status'
    NATIONALITY_KEY = 'nationality'

    def __init__(self, subject: Map = None):
        """Person Constructor

        Args:
            subject (Map): underlying map to
                which property calls are dispatched
        """
        self._subject: Map = subject or Map()
        if Person.FIRST_NAME_KEY not in self._subject.value:
            self._subject.add_item(Person.FIRST_NAME_KEY, String())
        if Person.LAST_NAME_KEY not in self._subject.value:
            self._subject.add_item(Person.LAST_NAME_KEY, String())

    @property
    def subject(self):
        return self._subject

    def _get_reference(self, key):
        if key not in self.subject.value:
            return None
        return self.subject.value[key]

    def _get_value(self, key):
        if key not in self.subject.value:
            return None
        return self.subject.value[key].value

    def _set_value(self, key, value):
        if key not in self.subject.value:
            instance = self.TEMPLATE.properties[key].create_instance()
            self.subject.add_item(key, instance)
        self.subject.value[key].value = value

    @property
    def courtesy_title(self) -> str:
        return self._get_value(self.COURTESY_TITLE_KEY)

    @courtesy_title.setter
    def courtesy_title(self, value: str):
        """An abbreviation of a person’s title, honorific, or salutation
            (such as Mr., Miss., Dr.,...).

        """
        self._set_value(Person.COURTESY_TITLE_KEY, value)

    @property
    def first_name(self) -> str:
        return self._get_value(self.FIRST_NAME_KEY)

    @first_name.setter
    def first_name(self, value: str):
        self._set_value(self.FIRST_NAME_KEY, value)

    @property
    def middle_name(self) -> str:
        return self._get_value(self.MIDDLE_NAME_KEY)

    @middle_name.setter
    def middle_name(self, value: str):
        self._set_value(self.MIDDLE_NAME_KEY, value)

    @property
    def last_name(self) -> str:
        return self._get_value(self.LAST_NAME_KEY)

    @last_name.setter
    def last_name(self, value: str):
        self._set_value(self.LAST_NAME_KEY, value)

    @property
    def suffix(self) -> str:
        return self._get_value(self.SUFFIX_KEY)

    @suffix.setter
    def suffix(self, value: str):
        """A group of letters provided after a person’s
        name to provide additional information
        (such as Jr., Sr., M.D., PhD, I, II, III,...).

        """
        self._set_value(self.SUFFIX_KEY, value)

    @property
    def personal_photo(self) -> Image:
        return Image(self._get_reference(self.PERSONAL_PHOTO_KEY))

    @personal_photo.setter
    def personal_photo(self, image: Image):
        self._set_value(self.PERSONAL_PHOTO_KEY, image.subject.value)

    @property
    def home_address(self) -> Address:
        return Address(self._get_reference(self.HOME_ADDRESS_KEY))

    @home_address.setter
    def home_address(self, address: Address):
        self._set_value(self.HOME_ADDRESS_KEY, address.subject.value)

    # @property
    # def birth_date(self) -> Date:
    #     return self._get_from_map('birth_date')
    #
    # @birth_date.setter
    # def birth_date(self, value: Date):
    #     self._set_value('birth_date', value)
    # TODO: Add Base Type Date to implement birth_date property

    @property
    def gender(self) -> String:
        return self._get_value(self.GENDER_KEY)

    @gender.setter
    def gender(self, value: String):
        """The gender identity of the person.
        The value of this property must be equal to one of the
        following known enum values:
                - female
                - male
                - not_specified
                - non_specific
            The default for this value is not_specified.
        """
        self._set_value(self.GENDER_KEY, value)

    @property
    def sex(self) -> String:
        return self._get_value(self.SEX_KEY)

    @sex.setter
    def sex(self, value: String):
        """The biological gender of the person.
                The value of this property must be equal to one of the
                 following known enum values:
                        - female
                        - male
                        - not_specified
                        - non_specific
                The default for this value is not_specified.
         """
        self._set_value(self.SEX_KEY, value)

    @property
    def marital_status(self) -> String:
        return self._get_value(self.MARITAL_STATUS_KEY)

    @marital_status.setter
    def marital_status(self, value: String):
        """Describes a person’s relationship with a significant other.
        The value of this property must be equal to one of the following
        enum values:
                - married
                - single
                - divorced
                - widowed
                - not_specified
            The default for this value is not_specified.
        """
        self._set_value(self.MARITAL_STATUS_KEY, value)

    @property
    def nationality(self) -> String:
        return self._get_value(self.NATIONALITY_KEY)

    @nationality.setter
    def nationality(self, value: String):
        """The legal relationship between a person and their state
         represented using the ISO 3166-1 Alpha-2 code.
        The format of this property must conform to this
         regular expression ^[A-Z]{2}$.
        """
        self._set_value(self.NATIONALITY_KEY, value)

    def __eq__(self, other) -> bool:
        return (
            self.courtesy_title,
            self.first_name,
            self.middle_name,
            self.last_name,
            self.suffix,
            self.gender,
            self.sex,
            self.marital_status,
            self.nationality
        ) == (
            other.courtesy_title,
            other.first_name,
            other.middle_name,
            other.last_name,
            other.suffix,
            other.gender,
            other.sex,
            other.marital_status,
            other.nationality
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        """Convert to string"""
        return str(self.courtesy_title) + ' ' + \
            str(self.first_name) + ' ' + \
            str(self.middle_name) + ' ' + \
            str(self.last_name) + ' ' + \
            str(self.suffix) + '\n' + \
            str(self.gender) + '\n' + \
            str(self.sex) + '\n' + \
            str(self.marital_status) + '\n' + \
            str(self.nationality)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Person({} {} {} {} {}, {}, {}, {}, {})'.format(
            self.courtesy_title,
            self.first_name,
            self.middle_name,
            self.last_name,
            self.suffix,
            self.gender,
            self.sex,
            self.marital_status,
            self.nationality
        )


Person.TEMPLATE = create_person_template()
