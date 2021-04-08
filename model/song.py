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

    def get_songs(self):
        db = self.database()
        c = db.cursor()
        c.execute("SELECT * FROM Song")
        songsList = c.fetchall()
        db.commit()
        c.close()
        db.close()
        return songsList

    def insert_song_rating(self, songID, username, rating):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO Rate (username, songID, Rating) VALUES (%s, %s, %s)"
        c.execute(sql, (username, songID, rating))
        db.commit()
        c.close()
        db.close()

    def get_song_rating(self, songID, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM Rate WHERE songID = %s AND username = %s"
        c.execute(sql, (songID, username))
        rating = c.fetchone()
        db.commit()
        c.close()
        db.close()
        return rating

    def update_song_rating(self, songID, username, rating):
        db = self.database()
        c = db.cursor()
        sql = "UPDATE Rate SET rating = %s WHERE songID = %s AND username = %s"
        c.execute(sql, (rating, songID, username))
        db.commit()
        c.close()
        db.close()

    def delete_song_rating(self, songID, username):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM Rate WHERE songID = %s AND username = %s"
        c.execute(sql, (songID, username))
        db.commit()
        c.close()
        db.close()

    def get_all_user_song_ratings(self, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM Rate WHERE username = %s"
        c.execute(sql, (username,))
        ratingList = c.fetchall()
        db.commit()
        c.close()
        db.close()
        return ratingList
