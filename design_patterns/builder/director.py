# from typing import TYPE_CHECKING

from builder.base_student_builder import BaseStudentBuilder

# if TYPE_CHECKING:
from builder.engineering_student_builder import EngineeringStudentBuilder
from builder.mba_student_builder import MBAStudentBuilder


class Director:
    def __init__(self, student_builder: BaseStudentBuilder) -> None:
        self.student_builder = student_builder

    def create_student(self) -> BaseStudentBuilder:
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self.create_engineering_student()

        elif isinstance(self.student_builder, MBAStudentBuilder):
            return self.create_mba_student()

        else:
            raise ValueError(f"Not found builder of type {str(BaseStudentBuilder)}")

    def create_engineering_student(self) -> EngineeringStudentBuilder:
        return (
            self.student_builder.set_roll_no(1)
            .set_age(20)
            .set_name("abc")
            .set_subjects()
            .build()
        )

    def create_mba_student(self) -> MBAStudentBuilder:
        return (
            self.student_builder.set_roll_no(2)
            .set_age(20)
            .set_name("def")
            .set_subjects()
            .build()
        )
