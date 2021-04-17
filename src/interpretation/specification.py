class Specification:
    def __init__(self, request_preview: bool= False):
        """Specification, specifies which interpretation is desired.

        This allows the manipulation of the interpreter such that the result
            better suites the envisioned use case of the interpretation.
            For example, the callee of the interpretation service can request
            previews.

        Args:
            request_preview (bool, optional): Specify if a preview is desired.
                Defaults to False.
        """
        self._is_request_for_preview = request_preview

    @property
    def is_request_for_preview(self) -> bool:
        """Property to query if this specification requests a preview.

        Returns:
            bool: true iff a preview has been ruested.
        """
        return self._is_request_for_preview
