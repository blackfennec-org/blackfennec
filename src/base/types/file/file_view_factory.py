# -*- coding: utf-8 -*-

from src.base.types.file.file_view_model import FileViewModel
from src.base.types.file.file_view import FileView


class FileViewFactory:
    """Creator of the FileView"""

    def create(self, interpretation) -> FileView:
        """creates a FileView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            FileView
        """
        view_model = FileViewModel(interpretation)
        return FileView(view_model)
