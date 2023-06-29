from abc import ABC, abstractmethod
from typing import Self


class BaseHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Self) -> Self:
        pass

    @abstractmethod
    def handle(self, log_type: str, log_message: str) -> str:
        pass
