from observer.email_observable import EmailObservable
from observer.phone_observer import PhoneObserver

if __name__ == "__main__":
    email_observable = EmailObservable()
    phone_observer = PhoneObserver()

    email_observable.register(phone_observer)
    email_observable.logic()



