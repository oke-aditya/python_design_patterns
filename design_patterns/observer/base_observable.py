from abc import ABC, abstractmethod

from observer.base_observers import BaseObservable 


class BaseObservable(ABC):
    """
    Base Class for all Observables.
    """

    @abstractmethod
    def register(self, observer: BaseObservable) -> None:
        pass
    
    @abstractmethod
    def remove(self, observer: BaseObservable) -> None:
        pass


    @abstractmethod
    def notify(self) -> None:
        pass


