from mysql.connector import connect
import hashlib



class VoteRepository:

    MYSQL_URI = "localhost"
    PORT = "3306"
    USERNAME = "admin"
    PASSWORD = "1234"
    DATABASE_NAME = "ma_bd"

    def __init__(self):
        self.connector = None
        try:
            self.__connect()
        except Exception as exception:
            print(exception)

    def __connect(self):
        self.connector = connect(host=self.MYSQL_URI, port=self.PORT, user=self.USERNAME, password=self.PASSWORD,
                                 database=self.DATABASE_NAME)
    def __verify_connection(self):
        if self.connector is None:
            self.__connect()
