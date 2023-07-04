from builder.base_student_builder import BaseStudentBuilder
from typing import Self


class MBAStudentBuilder(BaseStudentBuilder):
    def set_subjects(self) -> Self:
        subjects = ["accouts", "finance", "mgmt"]
        self.subjects = subjects
        return self
