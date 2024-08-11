# Memento Pattern

Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

It is used when we ned Undo functionality. Or when we need to restore the states or when we need snapshots.

We maintain the previous state in a memento.

There are 3 following classes.

1. Originator: The class whose state we want to save.
2. Memento: The object that stores the state.
3. Caretaker: The object that keeps track of the mementos and can restore the originator's state.

## Examples:

Text editors (where you might want to implement undo/redo functionality), games (where you may want to save and restore game states), and complex workflows or data processing systems (where checkpoints or snapshots of the state are needed).


```python

from memento.caretaker import CareTaker
from memento.text_editor import TextEditor


if __name__ == "__main__":
    text_editor = TextEditor()

    text_editor.type("Hello")    
    text_editor.type("World")

    print(f"Current Text: {text_editor.get_text()}")

    # Save the state
    care_taker = CareTaker()
    care_taker.save_memento(text_editor.save())

    # modify text
    text_editor.type("Welcome")

    print(f"New text = {text_editor.get_text()}")

    # Memento state is still saved
    restored_text = text_editor.restore(memento=care_taker.get_memento())

    print(f"Restored text = {restored_text}")

```
