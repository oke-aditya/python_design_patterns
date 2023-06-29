from abc import ABC, abstractmethod


class BasePasswordVault:
    @abstractmethod
    def create_password(self, enitlements: str, password: str) -> None:
        pass

    @abstractmethod
    def get_password(self, enitlements: str) -> str:
        pass
