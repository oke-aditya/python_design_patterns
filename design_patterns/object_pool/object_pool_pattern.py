from typing import Optional

from object_pool.db_conn import DBConnection

###
# Note that this class has to be singleton.
# You can use Singleton pattern / define this as __init__ of app so that it's created once.
###

class DBPoolConnectionManager:
    _free_connections: list[DBConnection] = []
    _used_connections: list[DBConnection] = []
    MAX_POOL_SIZE: int = 4
    MIN_POOL_SIZE: int = 3

    def __init__(self) -> None:
        for i in range(self.MIN_POOL_SIZE):
            self._free_connections.append(DBConnection())

    def get_connection(self) -> Optional[DBConnection]:
        if len(self._free_connections) == 0 and len(self._used_connections) >= self.MAX_POOL_SIZE:
            print("Connection Limit Exceeded cannot create more")
            return None

        elif len(self._free_connections) == 0 and len(self._used_connections) < self.MAX_POOL_SIZE:
            self._free_connections.append(DBConnection())
            print("Creating new connection")

        db_connection = self._free_connections.pop()
        self._used_connections.append(db_connection)
        print("Adding connection to used connection")
        return db_connection

    def release_db_connection(self, db_connection: DBConnection):
            if db_connection:
                self._used_connections.remove(db_connection)
                print("Removing DB connection")
                self._free_connections.append(db_connection) # Or maybe create new one
                print("Added back to free pool")
