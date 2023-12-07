import unittest
from database_handler import DatabaseHandler

"""
    A class for unit testing the DatabaseHandler class.

    This test class contains unit tests to verify the functionality of the 
    DatabaseHandler class. It includes tests for establishing database connections 
    and loading data from a database into a Pandas DataFrame. The tests ensure 
    that the DatabaseHandler class can successfully connect to a PostgreSQL 
    database, retrieve data from specified tables, and handle connections 
    appropriately.

    Methods:
    - test_connection: Tests if a connection to the database can be established.
    - test_load_data: Tests if data from a specified table can be loaded into a DataFrame.
    """

class TestDatabaseHandler(unittest.TestCase):
    
    def test_connection(self):
        """Test database connection."""
        db_handler = DatabaseHandler("localhost", "5432", "test_db", "user", "password")
        db_handler.connect()
        self.assertIsNotNone(db_handler.connection)
        db_handler.close()

    def test_load_data(self):
        """Test loading data from the database."""
        db_handler = DatabaseHandler("localhost", "5432", "test_db", "user", "password")
        db_handler.connect()
        df = db_handler.load_data('test_table')
        self.assertIsNotNone(df)
        db_handler.close()

if __name__ == '__main__':
    unittest.main()


# To run the tests, you would use the command line to execute the test module.
# Navigate to the directory containing your test_database_handler.py file and run:
    
# python -m unittest test_database_handler