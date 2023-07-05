from flyweight.letter_factory import LetterFactory

if __name__ == "__main__":
    lt = LetterFactory.create_character('a')
    lt.display(0, 0)

    lt2 = LetterFactory.create_character('a')
    lt2.display(0, 0)


    lt3 = LetterFactory.create_character('b')
    lt3.display(0, 0)

