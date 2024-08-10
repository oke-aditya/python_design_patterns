from collections.abc import Iterable
from typing import Any, Iterator
from iterator.alphabetical_iterator import AlphabeticalOrderIterator

class WordCollection(Iterable):
    """
    A compatible collection that has methods to add item and traverse
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index:int) -> Any:
        return self._collection[index]
    
    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, reverse=True)


    def add_item(self, item: Any) -> None:
        self._collection.append(item)


