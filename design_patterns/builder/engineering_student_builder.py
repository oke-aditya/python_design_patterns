from builder.base_student_builder import BaseStudentBuilder
from typing import Self


class EngineeringStudentBuilder(BaseStudentBuilder):
    def set_subjects(self) -> Self:
        subjects = ["DSA", "OOPS", "DBMS"]
        self.subjects = subjects
        return self
