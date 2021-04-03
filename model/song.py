import mysql.connector

from sqlsetup import *


class Song:

    def __init__(self, songID, name, genre, artist, duration):
        self.songID = songID
        self.name = name
        self.genre = genre
        self.artist = artist
        self.duration = duration


class SongManager:
    @staticmethod
    def database():
        db = mysql.connector.connect(
            host=SQLSetup.host,
            user=SQLSetup.user,
            password=SQLSetup.password,
            database=SQLSetup.db
        )
        return db

    def insert_song(self, song):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Song (songID, name, artist, duration, genre) VALUES (%s, %s, %s, %s, %s)"
        c.execute(sql, (song.songID, song.name, song.artist, song.duration, song.genre))
        db.commit()
        c.close()
        db.close()