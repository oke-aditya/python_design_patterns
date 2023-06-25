from observer.base_observable import BaseObservable
from observer.base_observers import BaseObserver


class EmailObservable(BaseObservable):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """


    _state: int = 0

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    _observers: list[BaseObserver] = []
    
    def register(self, observer: BaseObservable) -> None:
        self._observers.append(observer)
    
    def remove(self, observer: BaseObservable) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Updating the observers, due to change of state")
        for observer in self._observers:
            observer.update(self)

        self._state = 0
        print(f"Resetting the state after notifying new state = {self._state}")

    
    """
    Functionality that this observable has to do.
    """
    def logic(self) -> None:
        print("Recieved data, hence updating the state")
        self._state = 3
        self.notify()

