import unittest
import mysql.connector
from app.connect import connect

class TestConnect(unittest.TestCase):

    def test_connection(self):
        new_connection = connect(pwd='example123')
        # checks if the instance of the returned object is a database
        self.assertIsInstance(new_connection, mysql.connector.connection.MySQLConnection)


if __name__ == "__main__":
    unittest.main()