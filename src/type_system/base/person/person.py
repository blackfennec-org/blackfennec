# -*- coding: utf-8 -*-
import logging

from src.structure.map import Map
from src.structure.string import String
# from src.base.types.image import Image
# from src.base.types.address import Address
# from src.base.types.date import Date

logger = logging.getLogger(__name__)


class Person:
    """Person BaseType Class

    Helper class used by the person view_model representing
    the actual type 'Person'.
    Can be used by other classes as a helper to be able to
    include persons in a overlaying datatype.
    """

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
        return self._get_from_map('courtesy_title')

    @courtesy_title.setter
    def courtesy_title(self, value: String):
        """An abbreviation of a person’s title, honorific, or salutation
            (such as Mr., Miss., Dr.,...).

        """
        self._data['courtesy_title'] = value

    @property
    def first_name(self) -> String:
        return self._get_from_map('first_name')

    @first_name.setter
    def first_name(self, value: String):
        self._data['first_name'] = value

    @property
    def middle_name(self) -> String:
        return self._get_from_map('middle_name')

    @middle_name.setter
    def middle_name(self, value: String):
        self._data['middle_name'] = value

    @property
    def last_name(self) -> String:
        return self._get_from_map('last_name')

    @last_name.setter
    def last_name(self, value: String):
        self._data['last_name'] = value

    @property
    def suffix(self) -> String:
        return self._get_from_map('suffix')

    @suffix.setter
    def suffix(self, value: String):
        """A group of letters provided after a person’s
        name to provide additional information
        (such as Jr., Sr., M.D., PhD, I, II, III,...).

        """
        self._data['suffix'] = value

    # @property
    # def personal_photo(self) -> Image:
    #     return self._get_from_map('personal_photo')
    #
    # @personal_photo.setter
    # def personal_photo(self, value: Image):
    #     self._data['personal_photo'] = value
    # TODO: Add Base Type Image to implement birth_date property

    # @property
    # def home_address(self) -> Address:
    #     return self._get_from_map('home_address')
    #
    # @home_address.setter
    # def home_address(self, value: Address):
    #     self._data['home_address'] = value
    # TODO: Add Base Type Address to implement birth_date property

    # @property
    # def birth_date(self) -> Date:
    #     return self._get_from_map('birth_date')
    #
    # @birth_date.setter
    # def birth_date(self, value: Date):
    #     self._data['birth_date'] = value
    #TODO: Add Base Type Date to implement birth_date property

    @property
    def gender(self) -> String:
        return self._get_from_map('gender')

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
        self._data['gender'] = value

    @property
    def sex(self) -> String:
        return self._get_from_map('sex')

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
        self._data['sex'] = value

    @property
    def marital_status(self) -> String:
        return self._get_from_map('marital_status')

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
        self._data['marital_status'] = value

    @property
    def nationality(self) -> String:
        return self._get_from_map('nationality')

    @nationality.setter
    def nationality(self, value: String):
        """The legal relationship between a person and their state
         represented using the ISO 3166-1 Alpha-2 code.
        The format of this property must conform to this
         regular expression ^[A-Z]{2}$.
        """
        self._data['nationality'] = value

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

