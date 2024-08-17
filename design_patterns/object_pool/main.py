from object_pool.object_pool_pattern import DBPoolConnectionManager

if __name__ == '__main__':
    db_pool_conn_manager = DBPoolConnectionManager()
    db_conn1 = db_pool_conn_manager.get_connection()
    db_conn2 = db_pool_conn_manager.get_connection()
    db_conn3 = db_pool_conn_manager.get_connection()
    db_conn4 = db_pool_conn_manager.get_connection()
    db_conn5 = db_pool_conn_manager.get_connection()
    db_con = db_pool_conn_manager.release_db_connection(db_conn3)
