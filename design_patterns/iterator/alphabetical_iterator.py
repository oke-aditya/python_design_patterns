"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""

from collections.abc import Iterator
from typing import Any
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from iterator.word_collection import WordCollection

class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection: "WordCollection", reverse: bool = False) -> None:
        # Collection is a container which can hold values
        self._collection = collection
        # Stores logic if reverse iteration is needed
        self._reverse = reverse
        if reverse:
            self._position = -1
        else:
            self._position = 0
        
    
    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            if self._reverse:
                self._position += -1
            else:
                self._position += 1
        except IndexError:
            raise StopIteration()

        return value

