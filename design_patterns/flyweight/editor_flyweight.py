from flyweight.base_editor_flyweight import BaseProcessorFlyweight


class EditorFlyWeight(BaseProcessorFlyweight):
    
    def __init__(self, char: str, font_type: str, size: int) -> None:
        self.char = char
        self.font_type = font_type
        self.size = size

    def display(self, row: int, col: int) -> None:
        print(f"{self.char} is at {row} {col}")


