from singleton.db_conn import db_conn

if __name__ == "__main__":
    print(db_conn.get_conn())
