# This factory is crucial cache for Flyweight pattern
from flyweight.editor_flyweight import EditorFlyWeight

class LetterFactory:
    character_cache = {}

    @staticmethod
    def create_character(char: str) -> EditorFlyWeight:
        editor_flyweight = LetterFactory.character_cache.get(char)
        if editor_flyweight:
            return editor_flyweight
        else:
            editor_flyweight = EditorFlyWeight(char, font_type="Arial", size=10)
            LetterFactory.character_cache[char] = editor_flyweight
            return editor_flyweight



