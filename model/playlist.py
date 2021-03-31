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

    def get_playlist(self, name, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM Playlist WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        playlist = c.fetchone()
        db.commit()
        c.close()
        db.close()
        if playlist is None:
            return None
        return Playlist(playlist[0], playlist[1], playlist[[2]])

    def get_user_playlists(self, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT name FROM Playlist WHERE username = %s"
        c.execute(sql, (username,))
        playlists = c.fetchall()
        db.commit()
        c.close()
        db.close()
        return playlists

    def delete_playlist(self, name, username):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Playlist WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        print("playlist deleted")
        db.commit()
        c.close()
        db.close()

    def is_playlist_in_user(self, name, username):
        db = self.database()
        c = db.cursor(buffered=True)
        sql = "SELECT * FROM Playlist WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        db.commit()
        playlist = c.fetchone()
        c.close()
        db.close()
        if playlist is None:
            return False
        else:
            return True

    def insert_song_in_playlist(self, name, username, songID):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Contains (name, username, songID) VALUES (%s,%s,%d)"
        c.execute(sql, (name, username, songID))
        db.commit()
        c.close()
        db.close()

    def get_songs_in_playlist(self, name, username):
        db = self.database()
        c = db.cursor()
        c.execute(sql, (name, username, songID))
        sql = "SELECT songID FROM Contains WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        songsList = c.fetchall()
        db.commit()
        c.close()
        db.close()
        return songsList

    def delete_song_in_playlist(self, name, username, songID):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Contains WHERE name = %s AND username = %s AND songID = %d"
        c.execute(sql, (name, username, songID))
        print("song in playlist deleted")
        db.commit()
        c.close()
        db.close()
