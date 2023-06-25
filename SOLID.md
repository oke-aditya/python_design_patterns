# SOLID Principles in Low Level Design

1. Single Responsibility Principle (S)

Class should have only 1 reason to change.

Do not have bunch of methods in class which can change.

Try to modularize these methods into intefaces / abstract classes.

2. Open for Extension but Closed for Modification (O)

The main idea of this principle is to keep existing code from breaking when you implement new features.

The classes should be extensible. You can inherit other classes and add functionality, but not modify the existing the class and add bunch of methods.

Again use interfaces / abstract classes and the core code should extend them. Do not modify the core code classes and add bunch of functionality.

3. Liskov Substitution Principle (L)

If Class B inherits Class A. Then we can replace object of class A by object of class B without breaking the functionality.

If Class A has 3 functionalities.
Then SubClass B should have 3 functionalities and additional functionalities. 

Subclasses should not remove the original functionality.
 

4. Interface Segmented Principle (I)

Interfaces should be such that client should not implement unnecessary functionality.

Do not have intefaces / classes that add unnecessary functionality to the code when extended.

Keep them granular.

5. Dependency Injection / Inversion (D)


Classes should depend on interfaces / abstract classes than concretes classes. 

Adding concrete classes and extending them will limit functionality and make the code harder to change.

Use abstract classes / interfaces or best is generics / templates to extend functionality.

