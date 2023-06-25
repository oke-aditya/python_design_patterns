from abc import ABC, abstractmethod

from observer.base_observable import BaseObservable


class BaseObserver(ABC):
    """
    Base class for all observers
    """
    @abstractmethod
    def update(self, observable: BaseObservable) -> None:
        pass

