from proxy.login_password_vault_proxy import LoginPasswordVaultProxy

if __name__ == "__main__":
    login_proxy = LoginPasswordVaultProxy()
    login_proxy.create_password("ADMIN", "123")
    print(login_proxy.get_password("ADMIN"))

    login_proxy.create_password("USER", "123")
