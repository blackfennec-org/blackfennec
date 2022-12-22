class SpecificationMock:
    def __init__(self, request_preview: bool= False):
        self._is_request_for_preview = request_preview

    @property
    def is_request_for_preview(self) -> bool:
        return self._is_request_for_preview
