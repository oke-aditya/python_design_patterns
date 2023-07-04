# Singleton Pattern

Singleton is a creational design pattern that lets you ensure that a 
class has only one instance, while providing a global
access point to this instance.

# Note

There are debates, if singleton is considered as a good pattern or an anti-pattern.

It's even debated on how it should be implemented in Python.

The best way I feel is to create a module level object and import it.

This is thread safe, elegant, simple and works for Python.

https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons


# Use case

The Singleton pattern solves two problems at the same time, violating the Single Responsibility Principle:

Use the Singleton pattern when a class in your program should have just 
a single instance available to all clients; for example, a 
single database object shared by different parts of the program.

Use the Singleton pattern when you need stricter control over global variables.

# Example

```python

from singleton.db_conn import db_conn

if __name__ == "__main__":
    print(db_conn.get_conn())

```

