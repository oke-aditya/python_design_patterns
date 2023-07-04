# Builder Pattern

# Use Case




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

