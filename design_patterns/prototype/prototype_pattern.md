# Prototype Pattern

Prototype is a creational design pattern that lets you copy 
existing objects without making your code dependent on their classes.

# Use Case

Use the Prototype pattern when your code shouldn’t depend on the concrete classes of objects that you need to copy.

Use the pattern when you want to reduce the number of subclasses that only differ in the way they initialize their respective objects.

# Example

```python

from prototype.student import Student

if __name__ == "__main__":
    st = Student(age=10, roll_no=12)

    st_clone = st.clone()

    print(st_clone.age)
    print(st_clone.roll_no)
    print(st_clone.school)

```


