import mysql.connector

from config import *


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
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
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