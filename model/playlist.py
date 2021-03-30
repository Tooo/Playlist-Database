import mysql.connector


class Playlist:
    def __init__(self, name, username, date):
        self.name = name
        self.username = username
        self.date = date


class PublicPlaylist(Playlist):
    def __init__(self, name, username, date):
        super().__init__(name, username, date)


class PrivatePlaylist(Playlist):
    def __init__(self, name, username, date, password):
        super().__init__(name, username, date)
        self.password = password


class PlaylistManager:
    def database(self):
        db = mysql.connector.connect(
            host="localhost",
            user="user",
            password="password",
            database="playlistdatabase"
        )
        return db

    def insert_playlist(self, username, name, date):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Playlist (name,username,date) VALUES (%s,%s,%d)"
        c.execute(sql, (name, username, date))
        db.commit()
        c.close()
        db.close()

    def get_playlist(self, username, name):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM playlist WHERE username = %s AND name = %s"
        c.execute(sql, (username, name))
        user = c.fetchone()
        db.commit()
        c.close()
        db.close()
        if (user == None):
            return None
        return User(user[0])

    def delete_playlist(self, username, name):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Playlist WHERE username = %s AND name = %s"
        c.execute(sql, (username, name))
        print("record(s) deleted")
        db.commit()
        c.close()
        db.close()



