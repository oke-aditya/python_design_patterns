from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observer.base_observers import BaseObserver


class BaseObservable(ABC):
    """
    Base Class for all Observables.
    """

    @abstractmethod
    def register(self, observer: "BaseObserver") -> None:
        pass

    @abstractmethod
    def remove(self, observer: "BaseObserver") -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
