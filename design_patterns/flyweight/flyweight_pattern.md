# Fascade Pattern

Flyweight is a structural design pattern that lets you fit more objects into 
the available amount of RAM by sharing common parts of state between multiple objects 
instead of keeping all of the data in each object.

Separate the Intrinsic and Extrinsic Data.


This constant data of an object is usually called the intrinsic state. 

It lives within the object; other objects can only read it, not change it. 

The rest of the object’s state, often altered “from the outside” by other objects, is called the extrinsic state.

The Flyweight pattern suggests that you stop storing the extrinsic state inside the object. 

Since the same flyweight object can be used in different contexts, you have to make sure that its state can’t be modified. 

A flyweight should initialize its state just once, via constructor parameters. It shouldn’t expose any setters or public fields to other objects.

# Use Case

1. Design Word Processor / Text Editor
2. Design A Game with x, y coordinates.

# Example

```python



```
