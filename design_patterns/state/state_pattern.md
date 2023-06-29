# State Pattern


State is a behavioral design pattern that lets an object 
alter its behavior when its internal state changes. 

It appears as if the object changed its class.

The State pattern suggests that you create new classes for all possible states of an object 
and extract all state-specific behaviors into these classes.

To transition the context into another state, replace the active state 
object with another object that represents that new state. 
This is possible only if all state classes follow the same interface 
and the context itself works with these objects through that interface.

Use the State pattern when you have an object that behaves differently 
depending on its current state, the number of states is enormous, 
and the state-specific code changes frequently.


# Use cases

Anywhere where we can model states.

1. Design Vending Machine

2. Design TV

3. Design ATM

4. Design Video Player, Play music, Stop Music, Start music, Pause Music.


# Example

We first need to draw the state diagram for any given task.

Once we have the state diagram and clear requirements we can proceed to designing the classes.


![Vending Machine Diagram](../images/vending_machine_state_diagram.png)


