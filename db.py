import mysql.connector
from user import User


class DataBase(object):
    def __init__(self):
        self.db = None
        self.createConnector()

    def createConnector(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="attendance"
        )
        print(self.db)

    def createUser(self, name):
        mycursor = self.db.cursor()

        sql = "INSERT INTO users (fullname) VALUES ('" + name + "')"
        mycursor.execute(sql)
        self.db.commit()
        return self.getLastUser()

    def getLastUser(self):
        dbcursor = self.db.cursor()
        dbcursor.execute("SELECT * from users order by id desc limit 1")
        users = dbcursor.fetchall()
        user = None
        for row in users:
            user = User(id= row[0], fullname=row[1])
        return user

    def getAllUser(self):
        dbcursor = self.db.cursor()
        dbcursor.execute("SELECT * from users order by id asc")
        rows = dbcursor.fetchall()
        users = []
        for row in rows:
            users.append(User(id=row[0], fullname=row[1]))
        return users