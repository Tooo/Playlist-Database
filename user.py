import mysql.connector

class User:
    genres = []

    def __init__(self, username):
        self.username = username

class UserGenre:
    def __init__(self, username, genre):
        self.username = username
        self.genre = genre

class UserManager:
    def database(self):
        db = mysql.connector.connect(
            host = "localhost",
            user = "user",
            password = "password",
            database = "playlistdatabase"
        )
        return db

    def insert_user(self, user):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO user (username) VALUES (%s)"
        val = user.username
        c.execute(sql, (val, ))
        db.commit()
        c.close()
        db.close()
    
    def get_user(self, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM user WHERE username = %s"
        c.execute(sql, (username, ))
        user = c.fetchone()
        db.commit()
        c.close()
        db.close()
        if (user == None):
            return None
        return User(user[0])
