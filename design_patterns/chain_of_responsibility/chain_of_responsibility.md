# Chain of responsibility Design Pattern

Linearly we need to handle different resposiblities.

E.g ATM Handler

Withdraw 2000 --> Handler 2000 ----> Handler 500 -----> Handler 100

Each pass their handling if they are unable to handle.


Client --------------> Handler / Processor / Reciever (implements) -> Conrete Handler 1 / 2  3

# Use cases

Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.

The pattern lets you link several handlers into one chain and, upon receiving a request, “ask” each handler whether it can process it. This way all handlers get a chance to process the request.

Use the pattern when it’s essential to execute several handlers in a particular order.

Since you can link the handlers in the chain in any order, all requests will get through the chain exactly as you planned.

Use the CoR pattern when the set of handlers and their order are supposed to change at runtime.


# Example

```python

def log(log_type: str, log_msg: str):
    info_logger = InfoLogger()
    error_logger = ErrorLogger()

    error_logger.set_next(info_logger)

    res = error_logger.handle(log_type, log_msg)
    print(res)


log("INFO", "This is some info")

```

Each message is handled appropriately we don't need to create 3 different type of loggers.

This is not same as factory pattern as this is doing **behavioral changes** not creational changes.
We create logger in only 1 way.


# Use cases

1. Design ATM
2. Design Logger
3. Design Vending Machine


