import mysql.connector

from sqlsetup import *


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
            host=SQLSetup.host,
            user=SQLSetup.user,
            password=SQLSetup.password,
            database=SQLSetup.db
        )
        return db

    def insert_playlist(self, playlist):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Playlist (name,username,date) VALUES (%s,%s,%d)"
        c.execute(sql, (playlist.name, playlist.username, playlist.date))
        db.commit()
        c.close()
        db.close()

    def get_playlist(self, username, name):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM playlist WHERE username = %s AND name = %s"
        c.execute(sql, (username, name))
        playlist = c.fetchone()
        db.commit()
        c.close()
        db.close()
        if playlist is None:
            return None
        return Playlist(playlist[0], playlist[1], playlist[[2]])

    def delete_playlist(self, username, name):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Playlist WHERE username = %s AND name = %s"
        c.execute(sql, (username, name))
        print("record(s) deleted")
        db.commit()
        c.close()
        db.close()
