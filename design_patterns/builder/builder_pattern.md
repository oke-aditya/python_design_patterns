# Builder Pattern

Builder is a creational design pattern that lets you construct complex objects step by step. 

The pattern allows you to produce different types and representations of an object using the same construction code.


# Use Case

Use when there are lot of parameters in constructor.

Use when there is an ordered way and creation is complex. E.g. `house.setFloor().setWalls().setRoof()`


# Example

```python

from builder.director import Director
from builder.engineering_student_builder import EngineeringStudentBuilder
d = Director(EngineeringStudentBuilder())

student = d.create_engineering_student()

print(student.roll_no)

print(student.name)

print(student.subjects)


```

