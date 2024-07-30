# Iterator Pattern

Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

E.g. Think of Java Collections. We have a single Iterator class that can be used to iterate over multiple data types.
we can iterate over TreeMap, HasedTreeSet, LinkedList etc.

The main idea of the Iterator pattern is to extract the traversal behavior of a collection into a separate object called an iterator.

Implement Iterator interface,
implement has_next and next methods.

There can be several Concrete iterator implementation classes.
