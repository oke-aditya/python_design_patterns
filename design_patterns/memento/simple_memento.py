from typing import Self


class Memento:
    def __init__(self: Self, text: str) -> None:
        self._text = text
    
    def get_saved_text(self: Self) -> str:
        return self._text

