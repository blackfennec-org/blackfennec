# -*- coding: utf-8 -*-
import pytest

from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.auction.double_coverage import CoverageMock
from doubles.black_fennec.structure.type.double_type import TypeMock
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer


def test_auction():
    type1 = TypeMock(coverage=CoverageMock(0.5))
    type2 = TypeMock(coverage=CoverageMock(1))
    
    types = [type1, type2]
    subject = Dummy('Structure')
    result = Auctioneer.auction(types, subject)
    assert type1 not in result
    assert type2 in result

def test_auction_with_no_fitting_offers():
    types = []
    subject = Dummy('Structure')
    with pytest.raises(KeyError):
        Auctioneer.auction(types, subject)

@pytest.mark.xfail(reason='functionality moved')
def test_only_satisfying_offers_are_considered():
    type1 = TypeMock(satisfies=False)
    type2 = TypeMock(satisfies=True)
    types = [type1, type2]
    subject = Dummy('Structure')
    result = auctioneer.auction(types, subject)
    assert factory2 in result
    assert factory1 not in result
