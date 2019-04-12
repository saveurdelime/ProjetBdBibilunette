from mysql.connector import connect
import hashlib



class BibiRepository:

    MYSQL_URI = "127.0.0.1"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "1234"
    DATABASE_NAME = "ma_bd"
    connector = None

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


    def get_tableLunette(self):
        self.__verify_connection()
        select_image = ("SELECT * FROM Lunette")
        cursor = self.connector.cursor()
        cursor.execute(select_image)
        data = cursor.fetchall()

        return data
    def get_image(self):
        self.__verify_connection()
        select_query = "SELECT image FROM Lunette "
        cursor = self.connector.cursor()
        cursor.execute(select_query)

        return [{'image': pic[0]} for pic in cursor]
