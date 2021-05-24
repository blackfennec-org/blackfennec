# -*- coding: utf-8 -*-
import logging

from src.visualisation.base.person.person import Person
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String

logger = logging.getLogger(__name__)


class PersonViewModel:
    """View model for base type Person."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        if not isinstance(interpretation.structure, Map):
            message = 'interpretation received should be of' \
                      ' super type Map, but is of type %s'
            logger.warning(message, type(interpretation.structure))
        self._model: Person = Person(interpretation.structure)

    @property
    def courtesy_title(self):
        """Property for courtesy title"""
        return self._model.courtesy_title

    @courtesy_title.setter
    def courtesy_title(self, value: String):
        self._model.courtesy_title = value

    @property
    def first_name(self):
        """Property for first name"""
        return self._model.first_name

    @first_name.setter
    def first_name(self, value: String):
        self._model.first_name = value

    @property
    def middle_name(self):
        """Property for middle name"""
        return self._model.middle_name

    @middle_name.setter
    def middle_name(self, value: String):
        self._model.middle_name = value

    @property
    def last_name(self):
        """Property for last name"""
        return self._model.last_name

    @last_name.setter
    def last_name(self, value: String):
        self._model.last_name = value

    @property
    def suffix(self):
        """Property for suffix"""
        return self._model.suffix

    @suffix.setter
    def suffix(self, value: String):
        self._model.suffix = value

    @property
    def gender(self):
        """Property for gender"""
        return self._model.gender

    @gender.setter
    def gender(self, value: String):
        self._model.gender = value

    @property
    def sex(self):
        """Property for sex"""
        return self._model.sex

    @sex.setter
    def sex(self, value: String):
        self._model.sex = value

    @property
    def marital_status(self):
        """Property for marital status"""
        return self._model.marital_status

    @marital_status.setter
    def marital_status(self, value: String):
        self._model.marital_status = value

    @property
    def nationality(self):
        """Property for nationality"""
        return self._model.nationality

    @nationality.setter
    def nationality(self, value: String):
        self._model.nationality = value
