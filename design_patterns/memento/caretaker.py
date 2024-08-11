from typing import Optional
from memento.simple_memento import Memento


class CareTaker:
    def __init__(self) -> None:
        self._memento: Optional[Memento] = None
    
    def save_memento(self, memento: Memento) -> None:
        self._memento = memento
    
    def get_memento(self) -> Optional[Memento]:
        return self._memento 
