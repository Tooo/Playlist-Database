import mysql.connector

from config import *


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
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        return db

    def insert_playlist(self, playlist):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Playlist (name,username,date) VALUES (%s,%s,playlist.date)"
        c.execute(sql, (playlist.name, playlist.username))
        sql = "INSERT INTO Public (name,username) VALUES (%s,%s)"
        c.execute(sql, (playlist.name, playlist.username))
        db.commit()
        c.close()
        db.close()

    def insert_playlist_with_name(self, name, username):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Playlist (name,username) VALUES (%s,%s)"
        c.execute(sql, (name, username))
        sql = "INSERT INTO Public (name,username) VALUES (%s,%s)"
        c.execute(sql, (name, username))
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
        sql = "INSERT INTO Contains (name, username, songID) VALUES (%s,%s,%s)"
        c.execute(sql, (name, username, songID))
        db.commit()
        c.close()
        db.close()

    def get_songs_in_playlist(self, name, username):
        db = self.database()
        c = db.cursor()
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
        db.commit()
        c.close()
        db.close()

    def make_private(self, name, username, password):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Public WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        sql = "INSERT INTO Private (name,username,password) VALUES (%s,%s,%s)"
        c.execute(sql, (name, username, password))
        db.commit()
        c.close()
        db.close()

    def make_public(self, name, username):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Private WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        sql = "INSERT INTO Public (name,username) VALUES (%s,%s)"
        c.execute(sql, (name, username))
        db.commit()
        c.close()
        db.close()

    def password_check(self, name, username, password):
        db = self.database()
        c = db.cursor()
        sql = "SELECT password FROM Private WHERE name = %s AND username = %s AND password =%s"
        c.execute(sql, (name, username, password))
        playlist = c.fetchone()
        c.close()
        db.close()
        if playlist is None:
            return False
        else:
            return True

    def is_private(self, name, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT name FROM Public WHERE name = %s AND username = %s"
        c.execute(sql, (name, username))
        playlist = c.fetchone()
        c.close()
        db.close()
        if playlist is None:
            return True
        else:
            return False

    def join_playlist(self, name, username, name2, username2, name3, username3):
        db = self.database()
        c = db.cursor()
        sql = "SELECT songID FROM Contains WHERE name = %s AND username = %s " \
              "UNION " \
              "SELECT songID FROM Contains WHERE name = %s AND username = %s"
        c.execute(sql, (name, username, name2, username2))
        new_playlist = c.fetchall()
        self.insert_playlist_with_name(name3, username3)
        for song in new_playlist:
            self.insert_song_in_playlist(name3, username3, song)

    def share_playlist(self, name, username, username2):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO share (name,username, superUsername) VALUES (%s,%s,%s)"
        c.execute(sql, (name, username, username2))
        c.close()
        db.close()

    def rate_playlist(self, rating, comment, name, username, username2):
        db = self.database()
        c = db.cursor()
        sql = "UPDATE share SET rating = %d AND comment = %s WHERE name = %s AND username = %s AND superUsername = %s"
        c.execute(sql, (rating, comment, name, username, username2))
        c.close()
        db.close()