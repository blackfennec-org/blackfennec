class BaseTypeMock:
    def __init__(self, subject):
        self._subject = subject
        self.subject_getter_count = 0

    @property
    def subject(self):
        self.subject_getter_count += 1
        return self._subject
