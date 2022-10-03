import pytest

from doubles.double_dummy import Dummy
from src.black_fennec.structure.reference_navigation.navigator import Navigator


class NavigatorSubclass(Navigator):
    def navigate(self, structure):
        return structure

    def __repr__(self):
        return 'NavigatorSubclass()'


@pytest.fixture()
def navigator():
    return NavigatorSubclass()


def test_navigator_equality(navigator):
    assert navigator == NavigatorSubclass()


def test_navigator_inequality(navigator):
    assert navigator != Dummy()


def test_navigator_hash(navigator):
    assert hash(navigator) == hash(NavigatorSubclass())
