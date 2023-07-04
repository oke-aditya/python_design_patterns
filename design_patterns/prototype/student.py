from prototype.prototype_base import BasePrototype

from typing import Self

class Student(BasePrototype):

    school = "abc"

    def __init__(self, age: int, roll_no: int) -> None:
        self.age = age
        self.roll_no = roll_no
    
    
    def clone(self) -> Self:
        return Student(self.age, self.roll_no)

