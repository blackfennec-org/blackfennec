class Specification:
    """Specification, specifies which interpretation is desired.

    This allows the manipulation of the interpreter such that the result
        better suites the envisioned use case of the interpretation.
        For example, the callee of the interpretation service can request
        previews.
    """

    def __init__(self, request_preview: bool = False):
        """Specification constructor

        Args:
            request_preview (bool, optional): Specify if a preview is desired.
                Defaults to False.
        """
        self._is_request_for_preview = request_preview

    @property
    def is_request_for_preview(self) -> bool:
        """Property to query if this specification requests a preview.

        Returns:
            bool: true iff a preview has been requested.
        """
        return self._is_request_for_preview

    def __repr__(self):
        return f'Specification(request_preview={self._is_request_for_preview})'

    def __eq__(self, o):
        return self.is_request_for_preview == o.is_request_for_preview
