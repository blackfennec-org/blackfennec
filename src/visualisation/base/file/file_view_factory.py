# -*- coding: utf-8 -*-
from src.visualisation.base.file.file_preview import FilePreview
from src.visualisation.base.file.file_view_model import FileViewModel
from src.visualisation.base.file.file_view import FileView
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class FileViewFactory:
    """Creator of the FileView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> FileView:
        """creates a FileView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            FileView
        """
        view_model = FileViewModel(interpretation)
        if specification.is_request_for_preview:
            return FilePreview(view_model)

        return FileView(view_model)
