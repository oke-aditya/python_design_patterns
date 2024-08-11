from abc import ABC, abstractmethod
from typing import override


class BaseExpression(ABC):
    @abstractmethod
    def interpret(self, context: 'Context') -> int:
        pass


# Terminal Expression
class NumberExpression(BaseExpression):
    def __init__(self, number: int) -> None:
        self.number = number

    @override
    def interpret(self, context: 'Context') -> int:
        return self.number


# Non-terminal Expression for addition
class AddExpression(BaseExpression):
    def __init__(self, left: BaseExpression, right: BaseExpression) -> None:
        self.left = left
        self.right = right

    @override
    def interpret(self, context: 'Context') -> int:
        return self.left.interpret(context) + self.right.interpret(context)


# Non-terminal Expression for subtraction
class SubtractExpression(BaseExpression):
    def __init__(self, left: BaseExpression, right: BaseExpression) -> None:
        self.left = left
        self.right = right

    @override
    def interpret(self, context: 'Context') -> int:
        return self.left.interpret(context) - self.right.interpret(context)


class Context:
    pass
