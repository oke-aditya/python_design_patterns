# Design Snakes & Ladders Game

Customization possible

1. Number of dice
2. Number of snakes
3. Number of Ladders
4. Number of Players

Game is fixed for now from 0 -> 100

# Understanding and UML

One way to do it is using classes by creating class for Board, Dice, Players, Interface for snakes ladders, etc.

![Snake and Ladders](<snake ladders UML.png>)


Other way is to create functions and simulate the game

# High Level Implementation


## Approach 1

This simply maintains players in a deque and simulates game.

Store the snake and ladders in hashmaps and we can run the game.


## Approach 2

Follow the UML and implement them, Then Call Board.play() method.
