from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

    # @abstractmethod
    # def redo(self) -> None:
    #     pass
