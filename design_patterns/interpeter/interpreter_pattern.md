# Interpreter Pattern

he Interpreter design pattern is a behavioral pattern used to define a grammar for a language and provide an interpreter that interprets sentences in the language. It’s useful for designing language interpreters, compilers,
or domain-specific languages (DSLs).

Expression: Abstract class that defines an interface for interpreting sentences.

Terminal Expression: Implements the grammar rules for terminals.

Non-Terminal Expression: Implements the grammar rules for non-terminals and usually contains references to other expressions.

# Example

Design arithmetic expression parser

Design a new DSL that does queries.


