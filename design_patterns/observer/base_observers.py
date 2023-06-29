from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observer.base_observable import BaseObservable


class BaseObserver(ABC):
    """
    Base class for all observers
    """

    @abstractmethod
    def update(self, observable: "BaseObservable") -> None:
        pass
