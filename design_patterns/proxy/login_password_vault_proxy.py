from proxy.login_password_vault import BasePasswordVault
from proxy.login_password_vault import LoginPasswordVault


class LoginPasswordVaultProxy(BasePasswordVault):
    password_vault = LoginPasswordVault()

    def create_password(self, enitlements: str, password: str) -> None:
        if enitlements == "ADMIN":
            print("Valid Entitlements creating password")
            self.password_vault.create_password(enitlements, password)
        else:
            raise ValueError(
                f"Incorrect entitlements found entitlements = {enitlements}"
            )

    def get_password(self, enitlements: str) -> str:
        if enitlements == "ADMIN":
            print("Valid Entitlements creating password")
            return self.password_vault.get_password(enitlements)
        else:
            raise ValueError(
                f"Incorrect entitlements found entitlements = {enitlements}"
            )
