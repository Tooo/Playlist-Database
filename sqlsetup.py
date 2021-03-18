import mysql.connector

class SQLSetup:
    def create_playlist_database(self):
        db = mysql.connector.connect(
            host = "localhost",
            user = "user",
            password = "password"
        )
        c = db.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS playlistdatabase")
        c.close()
        db.close()

    def create_all_tables(self):
        db = mysql.connector.connect(
            host = "localhost",
            user = "user",
            password = "password",
            database = "playlistdatabase"
        )
        self.create_song_table(db)
        self.create_user_table(db)
        self.create_playlist_table(db)
        self.create_public_playlist_table(db)
        self.create_private_playlist_table(db)
        # self.create_rate_table(db)
        # self.create_contains_table(db)
        # self.create_share_table(db)
        # self.create_user_genre_table(db)
        # self.create_song_genre_table(db)
        db.close()

    def create_song_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
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
        )""")
        c.close()

    def create_public_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Public (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES Playlist (username)
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
        )""")
        c.close()

    def create_rate_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()

    def create_contains_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()
    
    def create_contains_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()
    
    def create_share_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()\
    
    def create_user_genre_tabl(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()
    
    def create_song_genre_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()