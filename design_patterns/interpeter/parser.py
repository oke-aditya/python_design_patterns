from interpeter.expression import BaseExpression, NumberExpression, AddExpression, SubtractExpression


class Parser:
    def __init__(self, expression_string: str) -> None:
        self.tokens: list[str] = expression_string.split()
        self.stack: list = []

    def parse(self) -> BaseExpression:
        for token in self.tokens:
            if token.isdigit():
                # Push number as NumberExpression
                self.stack.append(NumberExpression(int(token)))
            elif token in {'+', '-'}:
                # Operators, pop two elements and create expression
                right = self.stack.pop()
                left = self.stack.pop()
                if token == '+':
                    self.stack.append(AddExpression(left, right))
                elif token == '-':
                    self.stack.append(SubtractExpression(left, right))
        # The final expression will be the only element in the stack
        return self.stack[0]