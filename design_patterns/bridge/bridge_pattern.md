# Bridge Pattern

Bridge is a structural design pattern that lets you split a large class or a 
set of closely related classes into two separate hierarchies—abstraction 
and implementation—which can be developed independently of each other.

# Use Case

Use the Bridge pattern when you want to divide 
and organize a monolithic class that has several variants of 
some functionality (for example, if the class can work with various database servers).

Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.


# Strategy vs Bridge

Strategy: Focuses on selecting and executing an algorithm from a family of algorithms at runtime.

Bridge: Focuses on separating an abstraction from its implementation to allow the two to vary independently.

Strategy: The focus is on the interchangeable behaviors or algorithms that can be switched at runtime.

Bridge: The focus is on the separation of abstraction and implementation, enabling both to evolve independently.


