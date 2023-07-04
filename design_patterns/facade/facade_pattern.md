# Fascade Pattern

Facade is a structural design pattern that provides a 
simplified interface to a library, a framework, or any other complex set of classes.


# Use Cases

Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem.

Use the Facade when you want to structure a subsystem into layers.


# Example

```python

from facade.employee_fascade import EmployeeFacade

ef = EmployeeFacade()
ef.get_employee_details()

```