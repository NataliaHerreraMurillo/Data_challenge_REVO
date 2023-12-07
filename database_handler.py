import pandas as pd
import psycopg2

"""
    A class for handling database operations.

    This class provides methods to connect to a PostgreSQL database, 
    load data into Pandas DataFrames, and close the connection.
    """

class DatabaseHandler:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )

    def load_data(self, table_name):
        if self.connection is not None:
            query = f"SELECT * FROM {table_name};"
            return pd.read_sql_query(query, self.connection)
        else:
            print("Database connection is not established.")
            return None

    def close(self):
        if self.connection is not None:
            self.connection.close()
