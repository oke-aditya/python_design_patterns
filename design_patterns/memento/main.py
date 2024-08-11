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

