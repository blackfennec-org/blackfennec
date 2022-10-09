import pytest

from doubles.double_dummy import Dummy
from src.black_fennec.structure.merge.merged import MergedList

@pytest.mark.xfail
def test_merged_list():
    merged_list = MergedList(Dummy(), Dummy())
    merged_list.value