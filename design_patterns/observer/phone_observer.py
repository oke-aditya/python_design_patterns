from observer.base_observable import BaseObservable
from observer.base_observers import BaseObserver


class PhoneObserver(BaseObserver):
    def update(self, observable: BaseObservable) -> None:
        if observable._state > 3:
            print("Reacted to the event")
