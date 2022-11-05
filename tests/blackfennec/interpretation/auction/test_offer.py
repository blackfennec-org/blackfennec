# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.type_system.double_type import TypeMock
from blackfennec.interpretation.auction.coverage import Coverage
from blackfennec.interpretation.auction.offer import Offer


@pytest.fixture
def subject():
    return StructureMock("Structure")


@pytest.fixture
def type():
    return TypeMock("StructureType")


@pytest.fixture
def offer(subject, type):
    offer = Offer(subject, type)
    return offer


def test_can_create_offer(offer):
    assert offer is not None


def test_subject_getter(offer, subject):
    assert offer.subject == subject


def test_specificity_getter(offer):
    assert offer.specificity == 0


def test_type_getter(offer, type):
    assert offer.type == type


def test_coverage_getter_simple(subject):
    type = TypeMock("StructureType", Coverage.COVERED)
    offer = Offer(subject, type)
    assert offer.coverage == Coverage.COVERED


def test_equal_offers_equality(subject):
    type = TypeMock("StructureType", Coverage.COVERED)
    offer = Offer(subject, type)
    other_offer = Offer(subject, type)
    assert offer == other_offer


def test_lower_than_equal(offer, subject, type):
    other_offer = Offer(subject, type)
    assert not offer < other_offer
    assert not other_offer < offer


def test_respects_inheritance_hierarchy(offer, subject, type):
    subtype = TypeMock("StructureType", super_type=type)
    more_specific_offer = Offer(subject, subtype)
    assert more_specific_offer > offer


def test_lower_than_with_different_subject(offer, type):
    other_subject = StructureMock("Structure2")
    other_offer = Offer(other_subject, type)
    with pytest.raises(ValueError):
        offer < other_offer  # pylint: disable=pointless-statement


def test_representation(offer):
    offer_repr = repr(offer)
    type_repr = repr(offer.type)
    assert type_repr in offer_repr
