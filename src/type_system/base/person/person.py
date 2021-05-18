# -*- coding: utf-8 -*-
import logging

from src.structure.map import Map
from src.structure.string import String
# from src.base.types.date import Date
from src.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.type_system.base.address.address import Address, create_address_template
from src.type_system.base.image.image import Image, create_image_template

logger = logging.getLogger(__name__)


def create_person_template():
    """Person Template
    Defines the format of the person
    """
    template_map = Map()
    template_map[Person.COURTESY_TITLE_KEY] = String()
    template_map[Person.FIRST_NAME_KEY] = String()
    template_map[Person.MIDDLE_NAME_KEY] = String()
    template_map[Person.LAST_NAME_KEY] = String()
    template_map[Person.LAST_NAME_KEY] = String()
    template_map[Person.SUFFIX_KEY] = String()
    template_map[Person.GENDER_KEY] = String()
    template_map[Person.SEX_KEY] = String()
    template_map[Person.MARITAL_STATUS_KEY] = String()
    template_map[Person.NATIONALITY_KEY] = String()

    template_factory = TemplateFactoryVisitor()
    template = template_map.accept(template_factory)

    template[Person.COURTESY_TITLE_KEY].optional = True
    template[Person.MIDDLE_NAME_KEY].optional = True
    template[Person.SUFFIX_KEY].optional = True
    template[Person.PERSONAL_PHOTO_KEY] = create_image_template()
    template[Person.PERSONAL_PHOTO_KEY].optional = True
    template[Person.HOME_ADDRESS_KEY] = create_address_template()
    template[Person.HOME_ADDRESS_KEY].optional = True
    template[Person.GENDER_KEY].optional = True
    template[Person.SEX_KEY].optional = True
    template[Person.MARITAL_STATUS_KEY].optional = True
    template[Person.NATIONALITY_KEY].optional = True
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

    def __init__(self, map_interpretation: Map = Map()):
        """Person Constructor

        Args:
            map_interpretation (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._data: Map = map_interpretation

    def _get_from_map(self, key):
        """Wrapper for map access

        Checks whether key is in map and if yes, it
        returns its value. Otherwise None is returned.

        Args:
            key (str): Key of value to check

        Returns:
            Info: Value at key in map
        """
        if key not in self._data:
            return None
        return self._data[key]

    @property
    def courtesy_title(self) -> String:
        return self._get_from_map(self.COURTESY_TITLE_KEY)

    @courtesy_title.setter
    def courtesy_title(self, value: String):
        """An abbreviation of a person’s title, honorific, or salutation
            (such as Mr., Miss., Dr.,...).

        """
        self._data[self.COURTESY_TITLE_KEY] = value

    @property
    def first_name(self) -> String:
        return self._get_from_map(self.FIRST_NAME_KEY)

    @first_name.setter
    def first_name(self, value: String):
        self._data[self.FIRST_NAME_KEY] = value

    @property
    def middle_name(self) -> String:
        return self._get_from_map(self.MIDDLE_NAME_KEY)

    @middle_name.setter
    def middle_name(self, value: String):
        self._data[self.MIDDLE_NAME_KEY] = value

    @property
    def last_name(self) -> String:
        return self._get_from_map(self.LAST_NAME_KEY)

    @last_name.setter
    def last_name(self, value: String):
        self._data[self.LAST_NAME_KEY] = value

    @property
    def suffix(self) -> String:
        return self._get_from_map(self.SUFFIX_KEY)

    @suffix.setter
    def suffix(self, value: String):
        """A group of letters provided after a person’s
        name to provide additional information
        (such as Jr., Sr., M.D., PhD, I, II, III,...).

        """
        self._data[self.SUFFIX_KEY] = value

    @property
    def personal_photo(self) -> Image:
        return self._get_from_map(self.PERSONAL_PHOTO_KEY)

    @personal_photo.setter
    def personal_photo(self, value: Image):
        self._data[self.PERSONAL_PHOTO_KEY] = value

    @property
    def home_address(self) -> Address:
        return self._get_from_map(self.HOME_ADDRESS_KEY)

    @home_address.setter
    def home_address(self, value: Address):
        self._data[self.HOME_ADDRESS_KEY] = value

    # @property
    # def birth_date(self) -> Date:
    #     return self._get_from_map('birth_date')
    #
    # @birth_date.setter
    # def birth_date(self, value: Date):
    #     self._data['birth_date'] = value
    # TODO: Add Base Type Date to implement birth_date property

    @property
    def gender(self) -> String:
        return self._get_from_map(self.GENDER_KEY)

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
        self._data[self.GENDER_KEY] = value

    @property
    def sex(self) -> String:
        return self._get_from_map(self.SEX_KEY)

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
        self._data[self.SEX_KEY] = value

    @property
    def marital_status(self) -> String:
        return self._get_from_map(self.MARITAL_STATUS_KEY)

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
        self._data[self.MARITAL_STATUS_KEY] = value

    @property
    def nationality(self) -> String:
        return self._get_from_map(self.NATIONALITY_KEY)

    @nationality.setter
    def nationality(self, value: String):
        """The legal relationship between a person and their state
         represented using the ISO 3166-1 Alpha-2 code.
        The format of this property must conform to this
         regular expression ^[A-Z]{2}$.
        """
        self._data[self.NATIONALITY_KEY] = value

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
