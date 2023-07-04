from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from builder.base_student_builder import BaseStudentBuilder


class Student:
    def __init__(self, student_builder: "BaseStudentBuilder") -> None:
        self.roll_no = student_builder.roll_no
        self.age = student_builder.age
        self.name = student_builder.name
        self.subjects = student_builder.subjects
