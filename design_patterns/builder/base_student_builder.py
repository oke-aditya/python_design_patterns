from abc import ABC, abstractmethod
from typing import Self
from builder.student import Student


class BaseStudentBuilder(ABC):
    roll_no, age, name, subjects = None, None, None, []

    @abstractmethod
    def set_roll_no(self, roll_no: int) -> Self:
        self.roll_no = roll_no
        return self

    @abstractmethod
    def set_age(self, age: int) -> Self:
        self.age = age
        return self

    @abstractmethod
    def set_name(self, name: str) -> Self:
        self.name = name
        return self

    @abstractmethod
    def set_subjects(self) -> Self:
        pass

    def build(self) -> Student:
        return Student(self)
