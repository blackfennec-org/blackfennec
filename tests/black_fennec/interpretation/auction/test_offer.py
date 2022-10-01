# -*- coding: utf-8 -*-
import pytest

from doubles.black_fennec.structure.double_structure import (
    StructureMock,
    StructureTypeMock,
)
from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.interpretation.auction.offer import Offer


@pytest.fixture
def subject():
    return StructureMock("Structure")


@pytest.fixture
def type():
    return StructureTypeMock("StructureType")


@pytest.fixture
def offer(subject, type):
    offer = Offer(subject, type)
    return offer


def test_can_create_offer(offer):
    assert offer is not None


def test_subject_getter(offer, subject):
    assert offer.subject == subject


@pytest.mark.xfail
def test_specificity_getter(offer):
    assert offer.specificity == -1


def test_type_getter(offer, type):
    assert offer.type == type


def test_coverage_getter_simple(subject):
    type = StructureTypeMock("StructureType", Coverage.COVERED)
    offer = Offer(subject, type)
    assert offer.coverage == Coverage.COVERED


def test_equal_offers_equality(subject):
    type = StructureTypeMock("StructureType", Coverage.COVERED)
    offer = Offer(subject, type)
    other_offer = Offer(subject, type)
    assert offer == other_offer


def test_lower_than_equal(offer, subject, type):
    other_offer = Offer(subject, type)
    assert not offer < other_offer
    assert not other_offer < offer

@pytest.mark.xfail
def test_respects_inheritance_hierarchy(offer, subject, type):
    lower_offer = Offer(subject, supertype)
    assert not offer < lower_offer
    assert lower_offer < offer


def test_lower_than_with_different_subject(offer, type):
    other_subject = StructureMock("Structure2")
    other_offer = Offer(other_subject, type)
    with pytest.raises(ValueError):
        offer < other_offer  # pylint: disable=pointless-statement


def test_representation(offer):
    offer_repr = repr(offer)
    type_repr = repr(offer.type)
    assert type_repr in offer_repr
