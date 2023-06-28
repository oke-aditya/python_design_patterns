from proxy.base_password_vault import BasePasswordVault

class LoginPasswordVault(BasePasswordVault):
    def create_password(self, enitlements: str, password: str) -> None:
        print("Password created")

    def get_password(self, enitlements: str) -> str:
        print("Returning password")
        return "abc123"

