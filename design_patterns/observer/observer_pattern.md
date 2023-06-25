# Observer Strategy

Observer is a behavioral design pattern that lets you define a subscription mechanism to 
notify multiple objects about any events that happen to the object they’re observing.


Once the event has occured or the condition is met we Notify the other object.

We have in general, two classes, observable and observer.

Observable is what can observer. 
E.g. Weather Update,

Observer will get notified when there is change in observer.
E.g. TV for weather update

There is 1 ---> N Relationship between observable and observor.

One observables can have multiple observors.

Change in state of observable is directly notified to observers.


Observable Interface  (Publisher)                            Observer Interface (Subscriber)

register(Observor obj)                                       update() / update(Observable obj)

remove(Observor obj)

notify()

setData()


# Code To use

```python
from observer.email_observable import EmailObservable
from observer.phone_observer import PhoneObserver

email_observable = EmailObservable()
phone_observer = PhoneObserver()

email_observable.register(phone_observer)
email_observable.logic()

```


# Use cases: -

1. Subscribe / Notify button.
2. Out of stock orders.



