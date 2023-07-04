class DbConnection:
    def __init__(self, conn: int) -> None:
        self.conn = conn

    def get_conn(self) -> int:
        return self.conn


db_conn = DbConnection(10)
