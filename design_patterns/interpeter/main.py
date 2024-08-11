from interpeter.expression import Context, BaseExpression
from interpeter.parser import Parser

if __name__ == "__main__":
    # Putting the Post-Fix notation wil work, Infix will need different parser.
    expression_string: str = "10 2 - 4 +"
    context: Context = Context()

    # Create a parser instance and parse the expression
    parser: Parser = Parser(expression_string)
    expression: BaseExpression = parser.parse()

    # Interpret the expression
    result: int = expression.interpret(context)
    print(f"The result of the expression '{expression_string}' is: {result}")
