import mysql.connector
import pandas as pd
from config import *


class SQLSetup:
    host = DB_HOST
    user = DB_USER
    password = DB_PASSWORD
    db = DB_DATABASE

    def create_playlist_database(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        c = db.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS playlistdatabase")
        c.close()
        db.close()

    def create_all_tables(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        self.create_song_table(db)
        self.create_user_table(db)
        self.create_playlist_table(db)
        self.create_public_playlist_table(db)
        self.create_private_playlist_table(db)
        self.create_rate_table(db)
        self.create_contains_table(db)
        self.create_share_table(db)
        self.create_user_genre_table(db)
        db.close()

    def create_song_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration VARCHAR(255), 
                        artist VARCHAR(255),
                        genre VARCHAR(255),
                        PRIMARY KEY (songID)
        )""")
        c.close()

    def create_user_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS User (
                        username VARCHAR(255), 
                        PRIMARY KEY (username)
        )""")
        c.close()

    def create_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Playlist (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        date VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES User (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def create_public_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Public (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES Playlist (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (name) REFERENCES Playlist (name)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def create_private_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Private (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        password VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES Playlist (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (name) REFERENCES Playlist (name)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def create_rate_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Rate (
                        username VARCHAR(255),
                        songID INTEGER,
                        Rating BOOLEAN, 
                        PRIMARY KEY (username, songID),
                        FOREIGN KEY (username) REFERENCES User (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (songID) REFERENCES Song (songID)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def create_contains_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Contains ( 
                        name VARCHAR(255), 
                        username VARCHAR(255),
                        songID INTEGER,
                        PRIMARY KEY (name, username, songID),
                        FOREIGN KEY (songID) REFERENCES Song (songID)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (name) REFERENCES Playlist (name)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (username) REFERENCES User (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def create_share_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Share (
                        username VARCHAR(255), 
                        name VARCHAR(255), 
                        superUsername VARCHAR(255),
                        rating BOOLEAN,
                        comment VARCHAR(255), 
                        PRIMARY KEY (username, name, superusername),
                        FOREIGN KEY (username) REFERENCES User (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (name) REFERENCES Playlist (name)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE,
                        FOREIGN KEY (superUsername) REFERENCES User (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def create_user_genre_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS UserGenre (
                        username VARCHAR(255), 
                        genre VARCHAR(255), 
                        PRIMARY KEY (username, genre),
                        FOREIGN KEY (username) REFERENCES User (username)
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
        )""")
        c.close()

    def import_songs(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        df = pd.read_csv('data/billboard.csv')
        for col, row in df.iterrows():
            songID = row['SongID']
            genre = row['Genre']
            duration = row['Duration']
            name = row['Name']
            artist = row['Artist']
            c = db.cursor()
            sql = "INSERT INTO Song (songID, name, artist, duration, genre) VALUES (%s, %s, %s, %s, %s)"
            c.execute(sql, (songID, name, artist, duration, genre))
            db.commit()
            c.close()
        db.close()

    def sql_trigger(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        self.create_user_audit(db)
        self.before_user_insert_trigger(db)
        self.before_user_update_trigger(db)
        self.before_user_delete_trigger(db)
        db.close()

    def create_user_audit(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS user_audit (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            username VARCHAR(255),
                            newUsername VARCHAR(255),
                            changeDate DATETIME,
                            action VARCHAR(50)
        )""")
        c.close()

    def before_user_insert_trigger(self, db):
        c = db.cursor()
        c.execute("""CREATE TRIGGER before_user_create
                        BEFORE INSERT ON user
                        FOR EACH ROW
                        INSERT INTO user_audit
                            SET action = 'insert',
                                username = NEW.username,
                                changeDate = NOW()
        """)
        c.close()

    def before_user_update_trigger(self, db):
        c = db.cursor()
        c.execute("""CREATE TRIGGER before_user_update
                        BEFORE UPDATE ON user
                        FOR EACH ROW
                        INSERT INTO user_audit
                            SET action = 'update',
                                username = OLD.username,
                                newUsername = NEW.username,
                                changeDate = NOW()
                """)
        c.close()

    def before_user_delete_trigger(self, db):
        c = db.cursor()
        c.execute("""CREATE TRIGGER before_user_delete
                        BEFORE DELETE ON user
                        FOR EACH ROW
                        INSERT INTO user_audit
                            SET action = 'delete',
                                username = OLD.username,
                                changeDate = NOW()
                """)
        c.close()



sqlSetup = SQLSetup()
sqlSetup.create_playlist_database()
sqlSetup.create_all_tables()
sqlSetup.import_songs()
sqlSetup.sql_trigger()
