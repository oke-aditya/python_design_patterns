# Proxy design pattern

Client is proxied via in intermediate object which sends request to Proxy object.

Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.

Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).

Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.

Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.

Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.

Adapter provides a different interface to the wrapped object, Proxy provides it with the same interface, and Decorator provides it with an enhanced interface.

Proxies can be marshalled. Chain of Proxies can be connected to send data to real object.



# Use cases

1. Reverse Proxy for websites.
2. Firewalls that can intercept the requests.
3. Caching, where real object is queried, but a cached object is returned.
4. Pre processing and Post processing. We need to do processing before and after the object is used.
   E.g. Centralized Logging


Centralized access controlling
Caching.
Preprocessing, Post processing.


# Example

```python


from proxy.login_password_vault_proxy import LoginPasswordVaultProxy

login_proxy = LoginPasswordVaultProxy()

login_proxy.create_password("ADMIN", "123")

print(login_proxy.get_password("ADMIN"))

print(login_proxy.get_password("USER"))

```

