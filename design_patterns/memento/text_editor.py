from memento.simple_memento import Memento
from typing import Self

class TextEditor:
    def __init__(self: Self) -> None:
        self.text = ""
    
    def type(self: Self, words: str) -> None:
        self.text += words
    
    def get_text(self: Self) -> str:
        return self.text
    
    def save(self: Self) -> 'Memento':
        return Memento(self.text)

    def restore(self: Self, memento: 'Memento') -> str:
        return memento.get_saved_text()
