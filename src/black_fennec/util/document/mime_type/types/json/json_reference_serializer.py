# -*- coding: utf-8 -*-
from src.black_fennec.structure.reference_navigation.child_navigator import ChildNavigator
from src.black_fennec.structure.reference_navigation.index_of_navigator import IndexOfNavigator
from src.black_fennec.structure.reference_navigation.navigator import Navigator
from src.black_fennec.structure.reference_navigation.parent_navigator import ParentNavigator
from src.black_fennec.structure.reference_navigation.sibling_offset_navigator import SiblingOffsetNavigator
from src.black_fennec.structure.reference_navigation.uri_navigator import UriNavigator


class JsonReferenceSerializer:
    @staticmethod
    def serialize(navigator_list: list[Navigator]):
        first_element = navigator_list[0]
        if isinstance(first_element, UriNavigator):
            return first_element.uri

        reference = ""
        level_navigation = 0
        for navigator in navigator_list:
            if isinstance(navigator, ParentNavigator):
                level_navigation += 1
                navigator_list.remove(navigator)
            else:
                break

        if level_navigation:
            reference = str(level_navigation)

        first_element = navigator_list[0]
        if isinstance(first_element, SiblingOffsetNavigator):
            sibling_offset = first_element.sibling_offset
            if sibling_offset < 0:
                reference += "-"
            else:
                reference += "+"
            reference += str(sibling_offset)

        if reference:
            reference += "/"

        for navigator in navigator_list:
            if isinstance(navigator, ChildNavigator):
                reference += str(navigator.subscript) + "/"
            elif isinstance(navigator, IndexOfNavigator):
                reference += "#"

        return reference
