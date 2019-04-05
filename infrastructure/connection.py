from mysql.connector import connect
import hashlib



class BibiRepository:

    MYSQL_URI = "127.0.0.1"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "1234"
    DATABASE_NAME = "Bibilunette"
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

    @staticmethod
    def get_tableLunette():

        try:
            c =
            query = " SELECT * FROM Lunette"
            print('"query = " SELECT * FROM Lunette')
            self.connector.execute(query)
            print("c.execute(query)")
            data = self.connector.fetchall()
            print("data = c.fetchall()")
            self.connector.close()
            print("c.close()")
            return render_template('bibilncatalogue.html', data=data)
        except Exception as e:
            print ("wow  nonononononononononononononononon")
            return (str(e))
