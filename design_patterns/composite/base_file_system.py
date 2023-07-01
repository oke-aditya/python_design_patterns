from abc import ABC, abstractmethod

class BaseFileSystem(ABC):
    @abstractmethod
    def ls(self) -> None:
        pass


