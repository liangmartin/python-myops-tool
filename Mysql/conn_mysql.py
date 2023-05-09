import mysql.connector
import configparser

class MySQL:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.config['MYSQL']['host'],
                                                      user=self.config['MYSQL']['user'],
                                                      password=self.config['MYSQL']['password'],
                                                      database=self.config['MYSQL']['database'])
            self.cursor = self.connection.cursor(buffered=True)
            print("Connected to the database.")
        except mysql.connector.Error as error:
            print(f"Failed to connect to the database: {error}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection to the database closed.")

    def get_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

if __name__ == '__main__':
    db = MySQL('config.ini')
    db.connect()
    results = db.get_all('SELECT * FROM users')
    for row in results:
        print(row)
    db.disconnect()



