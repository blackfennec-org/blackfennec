#import pytest

from doubles.double_dummy import Dummy
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.merge.merged import MergedList, MergedMap, MergedStructure
from src.black_fennec.structure.string import String

"""
@pytest.mark.skip(reason="Not implemented")
def test_merged_list():
    merged_list = MergedList(Dummy(), Dummy())
    merged_list.value
"""

# Could be enhanced with `hypothesis`
def test_merged_equivalence_string():
    t = MergedStructure(String("underlay"), String("overlay"))
    assert t == t

def test_merged_equivalence_map():
    t = MergedMap(Map({"a": String("underlay")}), Map({"b": String("overlay")}))
    assert t == t
