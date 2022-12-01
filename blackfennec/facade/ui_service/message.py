import math


def _calculate_timeout(text: str):
    words = text.split(" ")
    word_count = len(words)
    slow_reader_seconds_per_word = 0.6
    reading_time = word_count*slow_reader_seconds_per_word
    attention_delay = 1
    return math.ceil(attention_delay + reading_time)


class Message:
    def __init__(
            self,
            text: str,
            timeout: int = None,
            action_name: str = None,
            action_target: str = None
    ):
        self._text = text
        self._timeout = timeout or _calculate_timeout(text)
        self._action_name = action_name
        self._action_target = action_target

    @property
    def text(self) -> str:
        return self._text

    @property
    def timeout(self) -> int:
        return self._timeout

    @property
    def action_target(self) -> str:
        return self._action_target

    @property
    def action_name(self) -> str:
        return self._action_name
