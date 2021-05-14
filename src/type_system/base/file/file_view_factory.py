# -*- coding: utf-8 -*-

from src.type_system.base.file.file_view_model import FileViewModel
from src.type_system.base.file.file_view import FileView
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification


class FileViewFactory:
    """Creator of the FileView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
               _: Specification) -> FileView:
        """creates a FileView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            FileView
        """
        view_model = FileViewModel(interpretation)
        return FileView(view_model)
